Name:       xcb-proto
Version:    1.15
Release:    1
Summary:    XML-XCB protocol library
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The xcb-proto package provides the XML-XCB protocol descriptions that libxcb uses to generate the majority of its code and API. 

%prep
%setup -q

%build 
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64/
rm -rf %{buildroot}/lib

%files
/usr/share/xcb/
/usr/lib64/python3.11/site-packages/
/usr/lib64/pkgconfig/xcb-proto.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.15-1
- Version bump
