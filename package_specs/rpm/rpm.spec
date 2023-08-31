Name:       rpm
Version:    4.17.1
Release:    1
Summary:    The RPM Package Manager
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
The RPM Package Manager

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
/usr/include/rpm/
/usr/lib/rpm/
/usr/lib64/
/usr/share/locale/
/usr/share/man/
/usr/lib/python3.7/
/usr/etc/dbus-1/system.d/org.rpm.conf

%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 4.14.2.1-2
- Updated build to use python3
