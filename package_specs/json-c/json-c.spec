Name:       json-c
Version:    0.13.1
Release:    1
Summary:    A JSON implementation in C
License:    MIT
Source0:    json-c-0.13.1-20180305.tar.gz
Prefix:     /usr

%description
A JSON implementation in C

%prep
%setup -n json-c-json-c-0.13.1-20180305

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/json-c/arraylist.h
/usr/include/json-c/bits.h
/usr/include/json-c/debug.h
/usr/include/json-c/json.h
/usr/include/json-c/json_c_version.h
/usr/include/json-c/json_config.h
/usr/include/json-c/json_inttypes.h
/usr/include/json-c/json_object.h
/usr/include/json-c/json_object_iterator.h
/usr/include/json-c/json_pointer.h
/usr/include/json-c/json_tokener.h
/usr/include/json-c/json_util.h
/usr/include/json-c/json_visit.h
/usr/include/json-c/linkhash.h
/usr/include/json-c/printbuf.h
/usr/lib64/libjson-c.a
/usr/lib64/libjson-c.so
/usr/lib64/libjson-c.so.4
/usr/lib64/libjson-c.so.4.0.0
/usr/lib64/pkgconfig/json-c.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.13.1
- Initial RPM

