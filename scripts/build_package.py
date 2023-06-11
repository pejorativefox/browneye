#!/bin/python

import os
import sys
import glob
import subprocess
import configparser
import ntpath
import shutil
from pathlib import Path
from urllib.parse import urlparse


BASE_PATH = os.path.expanduser('~')


def set_term_title(title):
    """Sets the title of a POSIX terminal using escape codes.

    Args:
        param1 (str) title: the string to use as the terminal title.

    """
    print("\033]0;{}\a".format(title))


def get_md5(filename):
    """Get an md5 for a file on the filesystem by running the md5sum tool.

    Args:
        param1 (str) filename: the full path of the file

    Returns:
        str: the md5sum of the specified file.

    """
    md5 = subprocess.check_output(["md5sum", filename]).rstrip().decode('ascii').split(" ")[0]
    return md5


def parse_sources(sources_filename):
    """Parse a 'sources' file to get a list of files that need to be downloaded
    for a package.

    Args:
        param1 (str) sources_filename: the full path to a valid sources file

    Returns:
        list of (str:md5sum, str:url, str:override_filename) 
                or 
                (str:md5sum, str:url, bool:has_override)
    
    """
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
    """Check for cached, download, and verify a 'sources' file.

    Args:
        param1 (str) sources_file: The full path and filename of a sources file.

    """
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
        if os.path.isfile(BASE_PATH + "/rpmbuild/SOURCES/{}".format(filename)):
            print("  + Already present (cached)")
        else:
            print("Downloading to {}".format(BASE_PATH + "/rpmbuild/SOURCES/{}".format(filename)))
            subprocess.call(["wget", "-c", "-O", BASE_PATH +"/rpmbuild/SOURCES/{}".format(filename), url])
        target_md5 = get_md5(BASE_PATH + "/rpmbuild/SOURCES/{}".format(filename))
        if md5 == target_md5:
            print("  + md5 good")
        else:
            print("Bad md5: {}".format(target_md5))
            exit()


def build(path):
    """Download, verify, and build a spec file.

    Args:
        param1 (str) path: the full path and filename to a spec file to build.

    """
    path, spec = os.path.split(path)
    print("Building:", path)
    if os.path.isdir("{}/files".format(path)):
        print("- Has additional source files..")
        for f in glob.glob("{}/files/*".format(path)):
            print("  * Copying:", f)
            shutil.copy(f, BASE_PATH + "/rpmbuild/SOURCES")
    if os.path.isfile("{}/sources".format(path)):
        print("- Processing sources:")
        process_sources("{}/sources".format(path))
    else:
        print("WARNING: this package is missing a valid sources file!")
    set_term_title("Building ( {} )".format(spec))
    spec_with_path = "{}/{}".format(path, spec)
    comp_proc = subprocess.run(["rpmbuild", "-bb", "--clean", spec_with_path])
    if comp_proc.returncode != 0:
        print("Build process returned {}!".format(comp_proc.returncode))
        exit(comp_proc.returncode)


if __name__ == "__main__":
    path = sys.argv[1]
    build(path)
    exit(0)



