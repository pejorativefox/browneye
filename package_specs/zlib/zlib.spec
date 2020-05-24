Name:       zlib
Version:    1.2.11
Release:    1
Summary:    zlib compression library
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The zlib compression library.

%prep
%setup -q -a0

%build
./configure --libdir=%{_libdir} --includedir=%{_includedir} --prefix=%{_prefix}
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/zconf.h
/usr/include/zlib.h
/usr/lib64/libz.a
/usr/lib64/libz.so
/usr/lib64/libz.so.1
/usr/lib64/libz.so.1.2.11
/usr/lib64/pkgconfig/zlib.pc
/usr/share/man/man3/zlib.3.gz


%changelog
# let's skip this for now
