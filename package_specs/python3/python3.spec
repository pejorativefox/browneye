Name:       Python
Version:    3.7.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --enable-shared     \
           --with-system-expat \
           --with-system-ffi   \
           --without-ensurepip
%make_build

%install
rm -rf %{buildroot}
%make_install
chmod -v 755 %{buildroot}/usr/lib64/libpython3.7m.so
chmod -v 755 %{buildroot}/usr/lib64/libpython3.so
rm -vf %{buildroot}%{_infodir}/dir*
rm -vrf %{buildroot}/usr/lib/python3.7/site-packages/pip/_internal/models/__pycache__

%files
/usr/bin/2to3
/usr/bin/2to3-3.7
/usr/bin/idle3
/usr/bin/idle3.7
/usr/bin/pydoc3
/usr/bin/pydoc3.7
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.7
/usr/bin/python3.7-config
/usr/bin/python3.7m
/usr/bin/python3.7m-config
/usr/bin/pyvenv
/usr/bin/pyvenv-3.7
/usr/include/python3.7m/*
/usr/lib/python3.7/*
/usr/lib64/libpython3.7m.so
/usr/lib64/libpython3.7m.so.1.0
/usr/lib64/libpython3.so
/usr/lib64/pkgconfig/python-3.7.pc
/usr/lib64/pkgconfig/python-3.7m.pc
/usr/lib64/pkgconfig/python3.pc
/usr/lib64/python3.7/*
/usr/share/man/man1/python3.1.gz
/usr/share/man/man1/python3.7.1.gz

%changelog
# let's skip this for now
