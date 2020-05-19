Name:       mozjs
Version:    52.2.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}gnome1.tar.gz


%description
TODO

%prep
%setup -n mozjs-52.2.1gnome1

%build
pushd js/src
%configure  --with-intl-api     \
            --with-system-zlib  \
            --with-system-nspr  \
            --with-system-icu   \
            --enable-threadsafe \
            --enable-readline
%make_build
popd

%install    
rm -rf %{buildroot}
pushd js/src
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*
rm %{buildroot}%{_libdir}/libjs_static.ajs

%files
/usr/bin/js52
/usr/bin/js52-config
/usr/include/mozjs-52/
/usr/lib64/libmozjs-52.so
/usr/lib64/pkgconfig/mozjs-52.pc


%changelog
# let's skip this for now

