Name:       libseccomp
Version:    2.4.2
Release:    1
Summary:    Kernel syscall interface library
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Platform independent, interface to the Linux Kernel's syscall filtering mechanism. 

%prep
%setup -q 

%build
%configure --prefix=/usr --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/scmp_sys_resolver
/usr/include/seccomp-syscalls.h
/usr/include/seccomp.h
/usr/lib64/libseccomp.so
/usr/lib64/libseccomp.so.2
/usr/lib64/libseccomp.so.2.4.2
/usr/lib64/pkgconfig/libseccomp.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.4.2-1
- Version bump
