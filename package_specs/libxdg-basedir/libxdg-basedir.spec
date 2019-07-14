Name:       libxdg-basedir
Version:    1.2.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    libxdg-basedir_1.2.0.orig.tar.gz

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
/usr/include/basedir.h
/usr/include/basedir_fs.h
/usr/lib64/libxdg-basedir.a
/usr/lib64/libxdg-basedir.la
/usr/lib64/libxdg-basedir.so
/usr/lib64/libxdg-basedir.so.1
/usr/lib64/libxdg-basedir.so.1.2.0
/usr/lib64/pkgconfig/libxdg-basedir.pc

%changelog
# let's skip this for now

