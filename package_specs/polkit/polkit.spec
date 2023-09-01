Name:       polkit
Version:    123
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

%description
TODO

Requires: shadow >= 4.6

%post
groupadd -fg 27 polkitd &&
useradd -c "PolicyKit Daemon Owner" -d /etc/polkit-1 -u 27 \
        -g polkitd -s /bin/false polkitd

%prep
%setup -q

%build
mkdir build &&
cd    build &&

meson setup ..                            \
      --prefix=/usr                       \
      --buildtype=release                 \
      -Dman=true                          \
      -Dtests=true \
      -Dgtk_doc=false \
      -Dman=false 
ninja

%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/
/usr/include/polkit-1/
/usr/lib/
/usr/share/
/etc/pam.d/polkit-1

%changelog
* Sun May 10 2020 Chris Statzer <chris.statzer@qq.com> 0.115
- Updated post install to create proper polkitd user

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.115
- Initial RPM

