Name:       libgcrypt
Version:    1.10.2
Release:    1
Summary:    GnuPG crypto library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2


%description
The libgcrypt package contains a general purpose crypto library based on the code used in GnuPG. 

%prep
%setup -q

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/dumpsexp
/usr/bin/hmac256
/usr/bin/libgcrypt-config
/usr/bin/mpicalc
/usr/include/gcrypt.h
/usr/lib64/libgcrypt.so
/usr/lib64/libgcrypt.so.20
/usr/lib64/libgcrypt.so.20.4.2
/usr/lib64/pkgconfig/libgcrypt.pc
/usr/share/aclocal/libgcrypt.m4
/usr/share/info/gcrypt.info-1.gz
/usr/share/info/gcrypt.info-2.gz
/usr/share/info/gcrypt.info.gz
/usr/share/man/man1/hmac256.1.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.10.2-1
- Version bump


