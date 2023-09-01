Name:       libXrandr
Version:    1.5.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



%description
TODO

%prep
%setup -a 0


%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
 /usr/include/X11/extensions/Xrandr.h
/usr/lib64/libXrandr.a
/usr/lib64/libXrandr.so
/usr/lib64/libXrandr.so.2
/usr/lib64/libXrandr.so.2.2.0
/usr/lib64/pkgconfig/xrandr.pc
/usr/share/man/man3/XRRConfigCurrentConfiguration.3.gz
/usr/share/man/man3/XRRConfigCurrentRate.3.gz
/usr/share/man/man3/XRRConfigRates.3.gz
/usr/share/man/man3/XRRConfigRotations.3.gz
/usr/share/man/man3/XRRConfigSizes.3.gz
/usr/share/man/man3/XRRConfigTimes.3.gz
/usr/share/man/man3/XRRFreeScreenConfigInfo.3.gz
/usr/share/man/man3/XRRGetScreenInfo.3.gz
/usr/share/man/man3/XRRQueryExtension.3.gz
/usr/share/man/man3/XRRQueryVersion.3.gz
/usr/share/man/man3/XRRRootToScreen.3.gz
/usr/share/man/man3/XRRSelectInput.3.gz
/usr/share/man/man3/XRRSetScreenConfig.3.gz
/usr/share/man/man3/XRRSetScreenConfigAndRate.3.gz
/usr/share/man/man3/Xrandr.3.gz

%changelog
# let's skip this for now
