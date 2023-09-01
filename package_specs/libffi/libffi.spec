Name:       libffi
Version:    3.2.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' \
    -i include/Makefile.in

sed -e '/^includedir/ s/=.*$/=@includedir@/' \
    -e 's/^Cflags: -I${includedir}/Cflags:/' \
    -i libffi.pc.in
%configure --disable-static --with-gcc-arch=native
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/ffi.h
/usr/include/ffitarget.h
/usr/lib/libffi.so
/usr/lib/libffi.so.6
/usr/lib/libffi.so.6.0.4
/usr/lib64/pkgconfig/libffi.pc
/usr/share/info/libffi.info.gz
/usr/share/man/man3/ffi.3.gz
/usr/share/man/man3/ffi_call.3.gz
/usr/share/man/man3/ffi_prep_cif.3.gz
/usr/share/man/man3/ffi_prep_cif_var.3.gz


%changelog
# let's skip this for now
