#!/bin/python

import os
import glob
import subprocess
import ntpath
from pathlib import Path


if not os.path.isdir(".build_cache"):
    os.mkdir(".build_cache")

packages = glob.glob("package_specs/*")
num_packages = len(packages)
count = 0
for path in packages:
    count += 1
    print("\n+ Processing: {} ({}/{})".format(path, count, num_packages))
    for spec in glob.glob("{}/*.spec".format(path)):
        print("* {}".format(spec))
        if os.path.isfile(".build_cache/{}".format(ntpath.basename(spec))):
            print("- Build already done, cached.")
        else:
            comp_proc = subprocess.run(["python", "./scripts/build_package.py", spec])
            if comp_proc.returncode != 0:
                print("Build process returned {}!".format(comp_proc.returncode))
                exit(comp_proc.returncode)
            else:
                cache_file = ntpath.basename(spec)
                print("Caching build: {}".format(cache_file))
                Path(".build_cache/{}".format(cache_file)).touch()

