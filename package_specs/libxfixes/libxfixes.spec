Name:       libXfixes
Version:    5.0.3
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
/usr/include/X11/extensions/Xfixes.h
/usr/lib64/libXfixes.a
/usr/lib64/libXfixes.la
/usr/lib64/libXfixes.so
/usr/lib64/libXfixes.so.3
/usr/lib64/libXfixes.so.3.1.0
/usr/lib64/pkgconfig/xfixes.pc
/usr/share/man/man3/Xfixes.3.gz

%changelog
# let's skip this for now
