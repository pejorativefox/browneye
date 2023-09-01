Name:       cairo
Version:    1.17.8
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(cairo)

%description
TODO

%prep
%setup -q

%build
mkdir build-c
pushd build-c
meson setup --prefix=/usr \
  -Dfreetype=enabled \
  -Dfontconfig=enabled \
  -Dglib=enabled \
  -Dgtk_doc=false \
  -Dspectre=disabled \
  -Dsymbol-lookup=disabled \
  -Dtests=disabled \
  -Dxcb=enabled \
  -Dxlib=enabled \
  -Dxml=disabled
ninja
popd

%install    
pushd build-c
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/cairo-trace
/usr/include/
/usr/lib/

%changelog
# let's skip this for now

