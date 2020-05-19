echo "*** STRIPPING BINS ***"
BUILDROOT=$1

for f in `find $BUILDROOT -type f -executable -exec sh -c "file '{}' | grep -q 'not stripped'" \\; -print`
do
	strip -v -g $f
done
#xargs -t -n1 strip -v --strip-unneeded

