Name:       xf86-video-intel
Version:    20190208
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
sed -i "s/#define force_inline inline __attribute__((always_inline))/#define force_inline inline/" src/sna/compiler.h
./autogen.sh --prefix=/usr     \
             --enable-kms-only \
             --enable-uxa      \
             --mandir=/usr/share/man
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

mv -v %{buildroot}/usr/share/man/man4/intel-virtual-output.4 \
      %{buildroot}/usr/share/man/man1/intel-virtual-output.1 &&
      
sed -i '/\.TH/s/4/1/' %{buildroot}/usr/share/man/man1/intel-virtual-output.1

%files
/usr/local/bin/intel-virtual-output
/usr/local/lib/libIntelXvMC.la
/usr/local/lib/libIntelXvMC.so
/usr/local/lib/libIntelXvMC.so.1
/usr/local/lib/libIntelXvMC.so.1.0.0
/usr/local/lib/xorg/modules/drivers/intel_drv.la
/usr/local/lib/xorg/modules/drivers/intel_drv.so
/usr/local/libexec/xf86-video-intel-backlight-helper
/usr/local/share/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy
/usr/share/man/man4/intel-virtual-output.4.gz
/usr/share/man/man4/intel.4.gz


%changelog
# let's skip this for now

