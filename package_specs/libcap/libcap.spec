Name:       libcap
Version:    2.26
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed -i '/install.*STALIBNAME/d' libcap/Makefile
%make_build

%install    
rm -rf %{buildroot}
#%make_install
	
make install RAISE_SETFCAP=no \
             DESTDIR=%{buildroot} \
             LIBDIR=%{_libdir} \
             SBINDIR=%{_sbindir} \
             PKGCONFIGDIR=%{_libdir}/pkgconfig/

#chmod +x %{buildroot}/lib64/libcap.so.2.26

%files
/usr/include/sys/capability.h
/usr/lib64/libcap.so
/usr/lib64/libcap.so.2
/usr/lib64/libcap.so.2.26
/usr/lib64/pkgconfig/libcap.pc
/usr/lib64/security/pam_cap.so
/usr/sbin/capsh
/usr/sbin/getcap
/usr/sbin/getpcaps
/usr/sbin/setcap
/usr/share/man/

%changelog
# let's skip this for now
