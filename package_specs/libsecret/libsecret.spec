Name:       libsecret
Version:    0.18.8
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
TODO

%prep
%setup -a 0

%build
%configure --disable-static --disable-manpages --enable-gtk-doc-html
%make_build

%install    
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir

%files
/usr/bin/secret-tool
/usr/include/libsecret-1/libsecret/*
/usr/lib64/girepository-1.0/Secret-1.typelib
/usr/lib64/libsecret-1.la
/usr/lib64/libsecret-1.so
/usr/lib64/libsecret-1.so.0
/usr/lib64/libsecret-1.so.0.0.0
/usr/lib64/pkgconfig/libsecret-1.pc
/usr/lib64/pkgconfig/libsecret-unstable.pc
/usr/share/gir-1.0/Secret-1.gir
/usr/share/gtk-doc/html/libsecret-1/*
/usr/share/locale/*
/usr/share/vala/vapi/libsecret-1.deps
/usr/share/vala/vapi/libsecret-1.vapi

%changelog
# let's skip this for now

