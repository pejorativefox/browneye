Name:       libaio
Version:    0.3.112
Release:    1
Summary:    The libaio package is an asynchronous I/O facility ("async I/O", or "aio") that has a richer API and capability set than the simple POSIX async I/O facility. 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The libaio package is an asynchronous I/O facility ("async I/O", or "aio") that has a richer API and capability set than the simple POSIX async I/O facility. 

%prep
%setup

%build
sed -i '/install.*libaio.a/s/^/#/' src/Makefile
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/libaio.h
/usr/lib/libaio.so
/usr/lib/libaio.so.1
/usr/lib/libaio.so.1.0.1

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.3.112
- Initial RPM

