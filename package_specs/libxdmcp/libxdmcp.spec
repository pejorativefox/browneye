Name:       libXdmcp
Version:    1.1.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build 
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xdmcp.h
/usr/lib64/libXdmcp.a
/usr/lib64/libXdmcp.la
/usr/lib64/libXdmcp.so
/usr/lib64/libXdmcp.so.6
/usr/lib64/libXdmcp.so.6.0.0
/usr/lib64/pkgconfig/xdmcp.pc
/usr/share/doc/libXdmcp/xdmcp.xml

%changelog
# let's skip this for now
