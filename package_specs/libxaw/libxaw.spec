Name:       libxaw
Version:    1.0.15
Release:    1
Summary:    Xt widget set
License:    GPL3
Prefix:     /usr
Source0:    libXaw-%{version}.tar.xz

BuildRequires: libxmu, libxpm

%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.

%prep
%setup -q -n libXaw-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xaw/
/usr/lib64/libXaw.so
/usr/lib64/libXaw.so.6
/usr/lib64/libXaw.so.7
/usr/lib64/libXaw6.a
/usr/lib64/libXaw6.so
/usr/lib64/libXaw6.so.6
/usr/lib64/libXaw6.so.6.0.1
/usr/lib64/libXaw7.a
/usr/lib64/libXaw7.so
/usr/lib64/libXaw7.so.7
/usr/lib64/libXaw7.so.7.0.0
/usr/lib64/pkgconfig/xaw6.pc
/usr/lib64/pkgconfig/xaw7.pc
/usr/share/doc/libXaw/
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.0.15-1
- Version bump
