Name:       libfontenc
Version:    1.1.7
Release:    1
Summary:    X font encoding library.
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
X font encoding library.

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
/usr/include/X11/fonts/fontenc.h
/usr/lib64/libfontenc.a
/usr/lib64/libfontenc.so
/usr/lib64/libfontenc.so.1
/usr/lib64/libfontenc.so.1.0.0
/usr/lib64/pkgconfig/fontenc.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.7-1
- Version bump
