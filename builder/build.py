import logging

from db import PackageDatabase
from process import run_process
from package import discover_packages
from sources import parse_sources, fetch_sources

log = logging.getLogger("BUILD")


def build_package(package):
    log.info("Building Package ({})".format(package.name))
    sources = parse_sources(package.get_full_sources_path())
    if fetch_sources(sources) != True:
        return False
    cmd = ["rpmbuild", "-bb", "--clean", package.get_full_spec_path()]
    return_code = run_process(cmd)
    if return_code != 0:
        return False
    return True


def build_all():
    package_db = PackageDatabase()
    packages = discover_packages()

    for package in packages:
        package_db.add_package(package.name)

    for package in packages:
        if package_db.is_built(package.name):
            print(package.name, "is already built, skipping.")
        else:
            if build_package(package) == True:
                package_db.set_built(package.name)
            else:
                package_db.set_failed(package.name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    build_all()