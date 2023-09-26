Name:       libass
Version:    0.14.0
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --prefix=/usr --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/ass/ass.h
/usr/include/ass/ass_types.h
/usr/lib64/libass.so
/usr/lib64/libass.so.9
/usr/lib64/libass.so.9.0.2
/usr/lib64/pkgconfig/libass.pc

%changelog
# let's skip this for now
