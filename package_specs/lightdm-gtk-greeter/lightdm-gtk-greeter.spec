Name:       lightdm-gtk-greeter
Version:    2.0.3
Release:    1
Summary:    GTK+ greeter for LightDM
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
GTK+ greeter for LightDM

%prep
%setup

%build
export HAVE_EXO_CSOURCE=yes
LDM_CFLAGS="-Wno-declaration-after-statement \
            -Wno-error=deprecated-declarations \
	    -Wno-error=cast-function-type"

#export CXXFLAGS="$CXXFLAGS $LDM_CFLAGS"
#export RPM_OPT_FLAGS="%optflags $LDM_CFLAGS"

CFLAGS="$CFLAGS $LDM_CFLAGS" \
./configure   --prefix=/usr                 \
	      --libexecdir=/usr/lib/lightdm \
              --enable-kill-on-sigterm      \
	      --disable-libido              \
	      --disable-libindicator        \
	      --disable-static && make

%install
rm -rf %{buildroot}
%make_install

%files
   /usr/etc/lightdm/lightdm-gtk-greeter.conf
   /usr/sbin/lightdm-gtk-greeter
   /usr/share/doc/lightdm-gtk-greeter/sample-lightdm-gtk-greeter.css
   /usr/share/icons/hicolor/*
   /usr/share/locale/*
   /usr/share/xgreeters/lightdm-gtk-greeter.desktop

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.0.3
- Initial RPM

