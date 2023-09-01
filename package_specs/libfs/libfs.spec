Name:       libFS
Version:    1.0.7
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
/usr/include/X11/fonts/FSlib.h
/usr/lib64/libFS.a
/usr/lib64/libFS.so
/usr/lib64/libFS.so.6
/usr/lib64/libFS.so.6.0.0
/usr/lib64/pkgconfig/libfs.pc
/usr/share/doc/libFS/FSlib.txt

%changelog
# let's skip this for now
