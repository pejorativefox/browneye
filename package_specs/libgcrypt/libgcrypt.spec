Name:       libgcrypt
Version:    1.8.4
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2


%description
TODO

%prep
%setup -a 0

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
/usr/lib64/libgcrypt.so.20.2.4
/usr/share/aclocal/libgcrypt.m4
/usr/share/info/gcrypt.info-1.gz
/usr/share/info/gcrypt.info-2.gz
/usr/share/info/gcrypt.info.gz
/usr/share/man/man1/hmac256.1.gz

%changelog
# let's skip this for now

