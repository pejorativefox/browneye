Name:       nettle
Version:    3.4
Release:    1
Summary:    A low-level cryptographic library.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

Provides: libhogweed.so.4()(64bit), libhogweed.so.4(HOGWEED_4)(64bit)
Provides: libnettle.so.6()(64bit), libnettle.so.6(NETTLE_6)(64bit)

%description
The Nettle package contains a low-level cryptographic library that is designed 
to fit easily in many contexts. 

%prep
%setup

%build
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir

%files
/usr/include/nettle/*
/usr/bin/nettle-hash
/usr/bin/nettle-lfib-stream
/usr/bin/nettle-pbkdf2
/usr/bin/pkcs1-conv
/usr/bin/sexp-conv
/usr/lib64/libhogweed.so
/usr/lib64/libhogweed.so.4
/usr/lib64/libhogweed.so.4.4
/usr/lib64/libnettle.so
/usr/lib64/libnettle.so.6
/usr/lib64/libnettle.so.6.4
/usr/lib64/pkgconfig/hogweed.pc
/usr/lib64/pkgconfig/nettle.pc
/usr/share/info/nettle.info.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.4
- Initial RPM

