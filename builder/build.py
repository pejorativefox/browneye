from db import PackageDatabase
from process import run_process
from package import discover_packages
from sources import parse_sources, fetch_sources


def build_package(package):
    print("Building Package ({})".format(package.name))
    sources = parse_sources(package.get_full_sources_path())
    fetch_sources(sources)


def build_all():
    package_db = PackageDatabase()
    packages = discover_packages()

    for package in packages:
        package_db.add_package(package.name)

    for package in packages:
        if package_db.is_built(package.name):
            print(package.name, "is already built, skipping.")
        else:
            build_package(package)
        package_db.set_built(package.name)


if __name__ == "__main__":
    build_all()