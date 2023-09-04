Name:       bzip2
Version:    1.0.8
Release:    1
Summary:    bzip2 is a free and open-source file compression program
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
bzip2 is a free and open-source file compression program that uses the Burrows-Wheeler algorithm.

%prep
%setup -q -a0

%build
rm -rf %{buildroot}
sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile
make -f Makefile-libbz2_so
make clean
make
make PREFIX=%{buildroot}/usr install
mkdir -pv %{buildroot}/usr/lib64
cp -av libbz2.so.* %{buildroot}/usr/lib64
ln -sv libbz2.so.1.0.8 %{buildroot}/usr/lib64/libbz2.so

cp -v bzip2-shared %{buildroot}/usr/bin/bzip2
for i in %{buildroot}/usr/bin/{bzcat,bunzip2}; do
  ln -sfv bzip2 $i
done
rm -rf %{buildroot}/usr/lib

%files
/usr/bin/bunzip2
/usr/bin/bzcat
/usr/bin/bzcmp
/usr/bin/bzdiff
/usr/bin/bzegrep
/usr/bin/bzfgrep
/usr/bin/bzgrep
/usr/bin/bzip2
/usr/bin/bzip2recover
/usr/bin/bzless
/usr/bin/bzmore
/usr/lib64/libbz2.so
/usr/lib64/libbz2.so.1.0
/usr/lib64/libbz2.so.1.0.8
/usr/include/bzlib.h
/usr/share/man

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.0.8
- Version bump
