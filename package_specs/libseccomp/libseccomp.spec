Name:       libseccomp
Version:    2.4.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

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
# let's skip this for now
