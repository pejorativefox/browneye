Name:       npth
Version:    1.6
Release:    1
Summary:    POSIX/ANSI-C Scheduling library
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
POSIX/ANSI-C Scheduling library

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/npth-config
/usr/include/npth.h
/usr/lib64/libnpth.la
/usr/lib64/libnpth.so
/usr/lib64/libnpth.so.0
/usr/lib64/libnpth.so.0.1.2
/usr/share/aclocal/npth.m4

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.6
- Initial RPM

