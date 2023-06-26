#!/bin/env python

import sys

PODMAN_COMMAND = "podman run -it"
SPEC_MOUNT = "--mount=type=bind,source={},destination=/build/{},ro=true,z"
RPMBUILD_MOUNT = "--mount=type=bind,source=/home/daspork/rpmbuild/,destination=/root/rpmbuild/,z"
IMAGE = "browneye:latest {}"

BUILD_COMMAND = "sh -c \"dnf update --refresh && dnf builddep -y {} && rpmbuild -bb --clean {}\""
if __name__ == "__main__":
    source_file = sys.argv[1]
    dest_file = source_file.split("/")[-1]
    print(PODMAN_COMMAND.format(source_file, dest_file, BUILD_COMMAND.format(source_file, source_file)))
