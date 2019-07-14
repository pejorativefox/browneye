#!/bin/bash

dirs=($(find package_specs -type d))
for dir in "${dirs[@]}"; do
  pushd $dir
  for spec in $(find ./*.spec)
  do
    echo -en "\033]0;Building ( $spec )\a"
    echo "Building: $spec"
  done
  popd
done
