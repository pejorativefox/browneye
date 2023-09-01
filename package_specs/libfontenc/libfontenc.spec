Name:       libfontenc
Version:    1.1.3
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
/usr/include/X11/fonts/fontenc.h
/usr/lib64/libfontenc.a
/usr/lib64/libfontenc.so
/usr/lib64/libfontenc.so.1
/usr/lib64/libfontenc.so.1.0.0
/usr/lib64/pkgconfig/fontenc.pc

%changelog
# let's skip this for now
