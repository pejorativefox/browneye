Name:       libcap
Version:    2.69
Release:    1
Summary:    POSIX 1003.1e capabilities
License:    GPL2
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

Provides: libcap.so.2()(64bit)

%description
POSIX 1003.1e capabilities

%prep
%setup -q 

%build
sed -i '/install -m.*STA/d' libcap/Makefile
%make_build

%install    
rm -rf %{buildroot}
%make_install prefix=/usr
	
%files
/usr/include/sys/capability.h
/usr/include/sys/psx_syscall.h
/usr/lib64/libcap.so
/usr/lib64/libcap.so.2
/usr/lib64/libcap.so.2.69
/usr/lib64/libpsx.so
/usr/lib64/libpsx.so.2
/usr/lib64/libpsx.so.2.69
/usr/lib64/pkgconfig/libcap.pc
/usr/lib64/pkgconfig/libpsx.pc
/usr/sbin/capsh
/usr/sbin/getcap
/usr/sbin/getpcaps
/usr/sbin/setcap
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump
