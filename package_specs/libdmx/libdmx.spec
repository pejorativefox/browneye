Name:       libdmx
Version:    1.1.4
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
/usr/include/X11/extensions/dmxext.h
/usr/lib64/libdmx.a
/usr/lib64/libdmx.so
/usr/lib64/libdmx.so.1
/usr/lib64/libdmx.so.1.0.0
/usr/lib64/pkgconfig/dmx.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.4-1
- Version bump
