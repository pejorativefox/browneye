Name:       rpm
Version:    4.18.1
Release:    1
Summary:    RPM package manager
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Programs to manage, build and install using the RPM package format.

%prep
%setup -q

%build
export PYTHON=/bin/python3.11
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
/usr/bin/rpmlua
/usr/lib64/python3.11/site-packages/rpm-4.18.1-py3.11.egg-info
/usr/lib64/python3.11/site-packages/rpm/__init__.py
/usr/lib64/python3.11/site-packages/rpm/_rpm.so
/usr/lib64/python3.11/site-packages/rpm/transaction.py
/usr/lib64/librpm.so
/usr/lib64/librpm.so.9
/usr/lib64/librpm.so.9.4.0
/usr/lib64/librpmbuild.so
/usr/lib64/librpmbuild.so.9
/usr/lib64/librpmbuild.so.9.4.0
/usr/lib64/librpmio.so
/usr/lib64/librpmio.so.9
/usr/lib64/librpmio.so.9.4.0
/usr/lib64/librpmsign.so
/usr/lib64/librpmsign.so.9
/usr/lib64/librpmsign.so.9.4.0
/usr/lib64/pkgconfig/rpm.pc
/usr/include/rpm/
/usr/lib/rpm/
/usr/lib64/rpm-plugins/
/usr/share/locale/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 4.18.1-1
- Version bump

* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 4.14.2.1-2
- Updated build to use python3
