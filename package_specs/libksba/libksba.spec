Name:       libksba
Version:    1.3.5
Release:    1
Summary:    X.509 certificate library
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
X.509 certificate library

%prep
%setup

%build
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir

%files
/usr/bin/ksba-config
/usr/include/ksba.h
/usr/lib64/libksba.la
/usr/lib64/libksba.so
/usr/lib64/libksba.so.8
/usr/lib64/libksba.so.8.11.6
/usr/share/aclocal/ksba.m4
/usr/share/info/ksba.info.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.3.5
- Initial RPM

