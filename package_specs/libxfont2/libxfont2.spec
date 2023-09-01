Name:       libXfont2
Version:    2.0.3
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
%configure --disable-devel-docs
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/fonts/libxfont2.h
/usr/lib64/libXfont2.a
/usr/lib64/libXfont2.so
/usr/lib64/libXfont2.so.2
/usr/lib64/libXfont2.so.2.0.0
/usr/lib64/pkgconfig/xfont2.pc

%changelog
# let's skip this for now
