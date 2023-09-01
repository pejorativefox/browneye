Name:       bzip2
Version:    1.0.6
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%make_build -f Makefile-libbz2_so

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin %{buildroot}/usr/lib %{buildroot}/usr/share/man %{buildroot}/usr/include

cp -v bzip2-shared %{buildroot}/usr/bin/bzip2
# bins
for i in %{buildroot}/usr/bin/{bzcat,bunzip2}; do
  ln -sfv bzip2 $i
done
# libs
for i in {libbz2.so.1.0,libbz2.so.1.0.6}; do
  cp $i %{buildroot}/usr/lib/
done
# headers
cp bzlib.h %{buildroot}/usr/include/

%files
/usr/bin/bunzip2
/usr/bin/bzcat
/usr/bin/bzip2
/usr/include/bzlib.h
/usr/lib/libbz2.so.1.0
/usr/lib/libbz2.so.1.0.6

%changelog
# let's skip this for now
