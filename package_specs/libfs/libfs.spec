Name:       libfs
Version:    1.0.9
Release:    1
Summary:    X Font Service client library
License:    GPL3
Prefix:     /usr
Source0:    libFS-%{version}.tar.xz

%description
X Font Service client library

%prep
%setup -q -n libFS-%{version}


%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/fonts/FSlib.h
/usr/lib64/libFS.a
/usr/lib64/libFS.so
/usr/lib64/libFS.so.6
/usr/lib64/libFS.so.6.0.0
/usr/lib64/pkgconfig/libfs.pc
/usr/share/doc/libFS/FSlib.txt

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.0.9-1
- Version bump
