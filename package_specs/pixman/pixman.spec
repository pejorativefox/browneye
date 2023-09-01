Name:       pixman
Version:    0.38.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz



%description
TODO

%prep
%setup -a 0

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/pixman-1/pixman-version.h
/usr/include/pixman-1/pixman.h
/usr/lib64/libpixman-1.so
/usr/lib64/libpixman-1.so.0
/usr/lib64/libpixman-1.so.0.38.0
/usr/lib64/pkgconfig/pixman-1.pc


%changelog
# let's skip this for now

