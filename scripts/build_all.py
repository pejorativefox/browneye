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
            subprocess.run(["./scripts/build_package.py", spec])
            Path(".build_cache/{}".format(ntpath.basename(spec))).touch()

        
