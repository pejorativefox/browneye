#!/bin/bash

set -e

dirs=($(find package_specs -type d))
for dir in "${dirs[@]}"; do
  pushd $dir
  for spec in $(find *.spec)
  do
    echo -en "\033]0;Building ( $spec )\a"
    if [ -f "../../build_cache/$spec" ]; then
	echo "Already built: $spec"
    else
	if [ -d "./files" ]
        then
            echo "Found additional source files..."
            for file in $(find files/*)
            do
              echo "* Copying $file"
	      cp -v $file ~/rpmbuild/SOURCES
            done	      
        fi
    	rpmbuild -bb --clean $spec
	echo "done" > ../../build_cache/$spec
    fi
  done
  popd
done
