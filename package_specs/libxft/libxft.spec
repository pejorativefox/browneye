Name:       libXft
Version:    2.3.2
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
/usr/include/X11/Xft/Xft.h
/usr/include/X11/Xft/XftCompat.h
/usr/lib64/libXft.a
/usr/lib64/libXft.la
/usr/lib64/libXft.so
/usr/lib64/libXft.so.2
/usr/lib64/libXft.so.2.3.2
/usr/lib64/pkgconfig/xft.pc
/usr/share/man/man3/Xft.3.gz

%changelog
# let's skip this for now
