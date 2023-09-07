Name:       gobject-introspection
Version:    1.76.1
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
mkdir build
pushd build
meson setup --prefix=/usr \
            --buildtype=release \
            -Dcairo=disabled \
            -Ddoctool=disabled \
            -Dgtk_doc=false \
            ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd


%files -f ../../SOURCES/gobject-introspection.filelist

%changelog
# let's skip this for now

