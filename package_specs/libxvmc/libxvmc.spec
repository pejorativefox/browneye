Name:       libXvMC
Version:    1.0.10
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
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
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
/usr/share/doc/libXvMC/XvMC_API.txt

%changelog
# let's skip this for now
