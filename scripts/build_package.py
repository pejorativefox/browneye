#!/bin/python

import os
import glob
import subprocess
import configparser
import ntpath
import shutil
from pathlib import Path
from urllib.parse import urlparse


def set_term_title(title):
    print("\033]0;{}\a".format(title))


def get_md5(filename):
    md5 = subprocess.check_output(["md5sum", filename]).rstrip().decode('ascii').split(" ")[0]
    return md5


def parse_sources(sources_filename):
    fbuff = ""
    with open(sources_filename, "r") as fd:
        fbuff = fd.readlines()
    sources = []
    for line in fbuff:
        split_line = line.rstrip().split(" ")
        line_length = len(split_line)
        if line_length == 2 or line_length == 3:
            pass
        else:
            print("{} appears to have a mangled line...".format(sources_filename))
            exit()
        md5 = split_line[0]
        url = split_line[1]
        if len(split_line) == 3:
            filename = split_line[2]
        else:
            filename = None
        sources.append([md5, url, filename])
    return sources


def process_sources(sources_file):
    sources = parse_sources(sources_file)
    for source in sources:
        md5, url, override_filename = source
        if "filename" in sources:
            override_filename = sources["filename"]
        filename = ""
        if override_filename:
            filename = override_filename
        else:
            filename = os.path.basename(urlparse(url).path)
        if os.path.isfile("/root/rpmbuild/SOURCES/{}".format(filename)):
            print("  + Already present (cached)")
        else:
            print("Downloading to {}".format("/root/rpmbuild/SOURCES/{}".format(filename)))
            subprocess.call(["wget", "-c", "-O", "/root/rpmbuild/SOURCES/{}".format(filename), url])
        target_md5 = get_md5("/root/rpmbuild/SOURCES/{}".format(filename))
        if md5 == target_md5:
            print("  + md5 good")
        else:
            print("Bad md5: {}".format(target_md5))
            exit()


def build(path):
    print("Building:", spec)
    print("\033]0;Building ( {} )\a".format(spec))
    comp_proc = subprocess.run(["rpmbuild", "-bb", "--clean", spec])
    if comp_proc.returncode != 0:
        print("Build process returned {}!".format(comp_proc.returncode))
        exit()


if not os.path.isdir(".build_cache"):
    os.mkdir(".build_cache")

packages = glob.glob("package_specs/*")
num_packages = len(packages)
count = 0
for package in packages:
    count += 1
    print("\n+ Processing: {} ({}/{})".format(package, count, num_packages))
    if os.path.isdir("{}/files".format(package)):
        print("- Has additional source files..")
        for f in glob.glob("{}/files/*".format(package)):
            print("  * Copying:", f)
            shutil.copy(f, "/root/rpmbuild/SOURCES")
    if os.path.isfile("{}/sources".format(package)):
        print("- Processing sources:")
        process_sources("{}/sources".format(package))
    else:
        print("WARNING: this package is missing a valid sources file!")
    for spec in glob.glob("{}/*.spec".format(package)):
        if os.path.isfile(".build_cache/{}".format(ntpath.basename(spec))):
            print("- Build already done, cached.")
        else:
            build(spec)
