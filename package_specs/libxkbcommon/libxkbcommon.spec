Name:       libxkbcommon
Version:    1.5.0
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
mkdir build &&
cd    build &&

meson setup ..            \
      --prefix=/usr       \
      --buildtype=release \
       -Denable-docs=false \
       -Denable-wayland=false
ninja

%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin
/usr/libexec/
/usr/share/
/usr/include/
/usr/lib/

%changelog
# let's skip this for now

