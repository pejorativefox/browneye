Name:       libite
Version:    2.5.3
Release:    1
Summary:    That missing frog DNA you've been looking for 
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
Libite is a lightweight library of frog DNA that can be used to fill the gaps in any dinosaur project. It holds useful functions and macros developed by both Finit and the OpenBSD project.

%prep
%setup -q

%build
%configure 
%make_build

%install
%make_install

%files
/usr/include/libite/conio.h
/usr/include/libite/lite.h
/usr/include/libite/queue.h
/usr/include/libite/strdupa.h
/usr/include/libite/strlite.h
/usr/include/libite/strndupa.h
/usr/include/libite/strnlen.h
/usr/include/libite/tree.h
/usr/include/lite
/usr/lib64/libite.so.5
/usr/lib64/libite.so.5.3.2
/usr/lib64/libite.a
/usr/lib64/libite.so
/usr/lib64/pkgconfig/libite.pc
/usr/share/doc/libite/ChangeLog.md
/usr/share/doc/libite/LICENSE
/usr/share/doc/libite/README.md


%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.5.3-1
- Version bump
