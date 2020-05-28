Name:       cmake
Version:    3.17.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz



%description
TODO

%prep
%setup


%build
./configure --prefix=/usr        \
            --system-libs        \
            --mandir=/share/man  \
            --no-system-jsoncpp  \
            --no-system-librhash \
            --docdir=/share/doc/cmake
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
#rm -rf %{buildroot}/usr/share/cmake-3.13/Help/generator/


%files
/usr/bin/ccmake
/usr/bin/cmake
/usr/bin/cpack
/usr/bin/ctest
/usr/share/aclocal/cmake.m4
/usr/share/cmake-3.17/*
/usr/share/doc/cmake/Copyright.txt
/usr/share/doc/cmake/cmlibrhash/COPYING
/usr/share/doc/cmake/cmlibrhash/README
/usr/share/doc/cmake/cmsys/Copyright.txt

%changelog
* Wed May 13 2020 Chris Statzer <chris.statzer@qq.com> 3.17.2
- Upgrade to fix missing policys in newer version

