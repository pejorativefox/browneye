Name:       libxvmc
Version:    1.0.13
Release:    1
Summary:    Xlib-based X-Video Motion Compensation API.
License:    GPL3
Prefix:     /usr
Source0:    libXvMC-%{version}.tar.xz

BuildRequires: libxv

%description
Xlib-based X-Video Motion Compensation API.

%prep
%setup -q -n libXvMC-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/vldXvMC.h
/usr/include/X11/extensions/XvMClib.h
/usr/lib64/libXvMC.a
/usr/lib64/libXvMC.so
/usr/lib64/libXvMC.so.1
/usr/lib64/libXvMC.so.1.0.0
/usr/lib64/libXvMCW.a
/usr/lib64/libXvMCW.so
/usr/lib64/libXvMCW.so.1
/usr/lib64/libXvMCW.so.1.0.0
/usr/lib64/pkgconfig/xvmc.pc
/usr/lib64/pkgconfig/xvmc-wrapper.pc
/usr/share/doc/libXvMC/XvMC_API.txt

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.0.13-1
- Version bump
