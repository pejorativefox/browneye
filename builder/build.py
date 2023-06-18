import logging
import os
import glob
import shutil

from db import PackageDatabase
from process import run_process
from package import discover_packages
from sources import parse_sources, fetch_sources

log = logging.getLogger("BUILD")


class PackageBuilder(object):
    def __init__(self):
        self.package_db = PackageDatabase()
        self.packages = {}
        packages = discover_packages()
        for package in packages:
            self.package_db.add_package(package.name)
            self.packages[package.name] = package

    def _build_package(self, package):
        print("Building Package ({})".format(package.name))
        sources = parse_sources(package.get_full_sources_path())
        if fetch_sources(sources) != True:
            return False
        if os.path.isdir(package.get_files_path()):
            print("has files")
            files_path = "{}/*".format(package.get_files_path())
            for f in glob.glob(files_path):
                print("  * Copying:", f)
                shutil.copy(f, os.path.expanduser('~') + "/rpmbuild/SOURCES")
        cmd = ["rpmbuild", "-bb", "--clean", package.get_full_spec_path()]
        print("Running: ", cmd)
        return_code = run_process(cmd)
        if return_code != 0:
            return False
        return True


    def build_package(self, package_name):
        if package_name in self.packages:
            package = self.packages[package_name]
            if self._build_package(package) == True:
                self.package_db.set_built(package.name)
                print("Sucessfully built: ", package_name)
            else:
                self.package_db.set_failed(package.name)
                print("Failed to build: ", package_name)
        else:
            print("Package {} not found.".format(package_name))

    def build_all(self):
        for package_name in self.packages:
            if self.package_db.is_built(package_name):
                print(package_name, "is already built, skipping.")
            else:
                self.build_package(package_name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)