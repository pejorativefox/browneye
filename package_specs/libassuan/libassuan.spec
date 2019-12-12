Name:       libassuan
Version:    2.5.1
Release:    1
Summary:    GnuPG ipc library.
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
GnuPG ipc library.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/libassuan-config
/usr/include/assuan.h
/usr/lib64/libassuan.la
/usr/lib64/libassuan.so
/usr/lib64/libassuan.so.0
/usr/lib64/libassuan.so.0.8.1
/usr/share/aclocal/libassuan.m4
/usr/share/info/assuan.info.gz
/usr/share/info/dir

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.5.1
- Initial RPM

