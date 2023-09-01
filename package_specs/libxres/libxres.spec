Name:       libXres
Version:    1.2.0
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
/usr/include/X11/extensions/XRes.h
/usr/lib64/libXRes.a
/usr/lib64/libXRes.so
/usr/lib64/libXRes.so.1
/usr/lib64/libXRes.so.1.0.0
/usr/lib64/pkgconfig/xres.pc
/usr/share/man/man3/XRes.3.gz
/usr/share/man/man3/XResQueryClientPixmapBytes.3.gz
/usr/share/man/man3/XResQueryClientResources.3.gz
/usr/share/man/man3/XResQueryClients.3.gz
/usr/share/man/man3/XResQueryExtension.3.gz
/usr/share/man/man3/XResQueryVersion.3.gz

%changelog
# let's skip this for now
