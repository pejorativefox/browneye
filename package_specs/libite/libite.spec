Name:       libite
Version:    2.1.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
TODO

%prep
%setup -a 0

%build
%configure 
%make_build

%install
%make_install

%files
/usr/include/lite/conio.h
/usr/include/lite/lite.h
/usr/include/lite/queue.h
/usr/include/lite/strdupa.h
/usr/include/lite/strlite.h
/usr/include/lite/strndupa.h
/usr/include/lite/strnlen.h
/usr/include/lite/tree.h
/usr/lib64/libite.a
/usr/lib64/libite.la
/usr/lib64/libite.so
/usr/lib64/libite.so.5
/usr/lib64/libite.so.5.0.1
/usr/lib64/pkgconfig/libite.pc
/usr/share/doc/libite/ChangeLog.md
/usr/share/doc/libite/LICENSE
/usr/share/doc/libite/README.md


%changelog
# let's skip this for now
