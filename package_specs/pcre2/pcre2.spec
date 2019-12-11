Name:       pcre2
Version:    10.34
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
%configure  --prefix=/usr                       \
            --docdir=/usr/share/doc/pcre2-10.34 \
            --enable-unicode                    \
            --enable-jit                        \
            --enable-pcre2-16                   \
            --enable-pcre2-32                   \
            --enable-pcre2grep-libz             \
            --enable-pcre2grep-libbz2           \
            --enable-pcre2test-libreadline      \
            --disable-static 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/pcre2-config
/usr/bin/pcre2grep
/usr/bin/pcre2test
/usr/include/pcre2.h
/usr/include/pcre2posix.h
/usr/lib64/libpcre2-16.la
/usr/lib64/libpcre2-16.so
/usr/lib64/libpcre2-16.so.0
/usr/lib64/libpcre2-16.so.0.9.0
/usr/lib64/libpcre2-32.la
/usr/lib64/libpcre2-32.so
/usr/lib64/libpcre2-32.so.0
/usr/lib64/libpcre2-32.so.0.9.0
/usr/lib64/libpcre2-8.la
/usr/lib64/libpcre2-8.so
/usr/lib64/libpcre2-8.so.0
/usr/lib64/libpcre2-8.so.0.9.0
/usr/lib64/libpcre2-posix.la
/usr/lib64/libpcre2-posix.so
/usr/lib64/libpcre2-posix.so.2
/usr/lib64/libpcre2-posix.so.2.0.3
/usr/lib64/pkgconfig/libpcre2-16.pc
/usr/lib64/pkgconfig/libpcre2-32.pc
/usr/lib64/pkgconfig/libpcre2-8.pc
/usr/lib64/pkgconfig/libpcre2-posix.pc
/usr/share/doc/pcre2-10.34/*
/usr/share/man/*

%changelog
# let's skip this for now

