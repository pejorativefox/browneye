Name:       libXpm
Version:    3.5.12
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
/usr/bin/cxpm
/usr/bin/sxpm
/usr/include/X11/xpm.h
/usr/lib64/libXpm.a
/usr/lib64/libXpm.so
/usr/lib64/libXpm.so.4
/usr/lib64/libXpm.so.4.11.0
/usr/lib64/pkgconfig/xpm.pc
/usr/share/man/man1/cxpm.1.gz
/usr/share/man/man1/sxpm.1.gz


%changelog
# let's skip this for now
