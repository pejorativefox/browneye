Name:       liblzo2
Version:    2.10
Release:    1
Summary:    LZO is a portable lossless data compression library written in ANSI C.
License:    GPL
Source0:    lzo-%{version}.tar.gz
Prefix:     /usr

%description
LZO is a portable lossless data compression library written in ANSI C.

%prep
%setup -n lzo-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/lzo/
/usr/lib64/liblzo2.a
/usr/lib64/liblzo2.la
/usr/lib64/pkgconfig/lzo2.pc
/usr/share/doc/lzo/

%changelog
* Wed Aug 19 2020 Chris Statzer <chris.statzer@qq.com> 2.10
- Initial RPM

