Name:       rpm
Version:    4.14.2.1
Release:    2
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
export PYTHON=/bin/python3.7
%configure --without-lua --enable-python
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/gendiff
/usr/bin/rpm
/usr/bin/rpm2archive
/usr/bin/rpm2cpio
/usr/bin/rpmbuild
/usr/bin/rpmdb
/usr/bin/rpmgraph
/usr/bin/rpmkeys
/usr/bin/rpmquery
/usr/bin/rpmsign
/usr/bin/rpmspec
/usr/bin/rpmverify
/usr/include/rpm/*
/usr/lib/rpm/
/usr/lib64/librpm.la
/usr/lib64/librpm.so
/usr/lib64/librpm.so.8
/usr/lib64/librpm.so.8.1.0
/usr/lib64/librpmbuild.la
/usr/lib64/librpmbuild.so
/usr/lib64/librpmbuild.so.8
/usr/lib64/librpmbuild.so.8.1.0
/usr/lib64/librpmio.la
/usr/lib64/librpmio.so
/usr/lib64/librpmio.so.8
/usr/lib64/librpmio.so.8.1.0
/usr/lib64/librpmsign.la
/usr/lib64/librpmsign.so
/usr/lib64/librpmsign.so.8
/usr/lib64/librpmsign.so.8.1.0
/usr/lib64/pkgconfig/rpm.pc
/usr/lib64/rpm-plugins/
/usr/share/locale/
/usr/share/man/
/usr/lib64/rpm-plugins/systemd_inhibit.la
/usr/lib64/rpm-plugins/systemd_inhibit.so
/usr/lib/python3.7/

%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 4.14.2.1-2
- Updated build to use python3
