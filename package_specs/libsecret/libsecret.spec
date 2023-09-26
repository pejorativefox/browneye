Name:       libsecret
Version:    0.21.0
Release:    1
Summary:    GObject secret service library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

BuildRequires: libxslt

%description
The libsecret package contains a GObject based library for accessing the Secret Service API.

%prep
%setup -q

%build
mkdir build-libsecret
pushd build-libsecret
meson setup --prefix=/usr       \
            --buildtype=release \
            -Dgtk_doc=false     \
            -Dmanpage=false     \
            -Dintrospection=false \
            ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-libsecret
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir

%files
/usr/bin/secret-tool
/usr/include/libsecret-1/libsecret/
/usr/lib64/libsecret-1.so
/usr/lib64/libsecret-1.so.0
/usr/lib64/libsecret-1.so.0.0.0
/usr/lib64/pkgconfig/libsecret-1.pc
/usr/lib64/pkgconfig/libsecret-unstable.pc
/usr/share/locale/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.21.0-1
- Version bump

