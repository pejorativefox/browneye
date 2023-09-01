Name:       libXxf86vm
Version:    1.1.4
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
/usr/include/X11/extensions/xf86vmode.h
/usr/lib64/libXxf86vm.a
/usr/lib64/libXxf86vm.so
/usr/lib64/libXxf86vm.so.1
/usr/lib64/libXxf86vm.so.1.0.0
/usr/lib64/pkgconfig/xxf86vm.pc
/usr/share/man/man3/XF86VM.3.gz
/usr/share/man/man3/XF86VidModeAddModeLine.3.gz
/usr/share/man/man3/XF86VidModeDeleteModeLine.3.gz
/usr/share/man/man3/XF86VidModeGetAllModeLines.3.gz
/usr/share/man/man3/XF86VidModeGetDotClocks.3.gz
/usr/share/man/man3/XF86VidModeGetGamma.3.gz
/usr/share/man/man3/XF86VidModeGetGammaRamp.3.gz
/usr/share/man/man3/XF86VidModeGetGammaRampSize.3.gz
/usr/share/man/man3/XF86VidModeGetModeLine.3.gz
/usr/share/man/man3/XF86VidModeGetMonitor.3.gz
/usr/share/man/man3/XF86VidModeGetPermissions.3.gz
/usr/share/man/man3/XF86VidModeGetViewPort.3.gz
/usr/share/man/man3/XF86VidModeLockModeSwitch.3.gz
/usr/share/man/man3/XF86VidModeModModeLine.3.gz
/usr/share/man/man3/XF86VidModeQueryExtension.3.gz
/usr/share/man/man3/XF86VidModeQueryVersion.3.gz
/usr/share/man/man3/XF86VidModeSetClientVersion.3.gz
/usr/share/man/man3/XF86VidModeSetGamma.3.gz
/usr/share/man/man3/XF86VidModeSetGammaRamp.3.gz
/usr/share/man/man3/XF86VidModeSetViewPort.3.gz
/usr/share/man/man3/XF86VidModeSwitchMode.3.gz
/usr/share/man/man3/XF86VidModeSwitchToMode.3.gz
/usr/share/man/man3/XF86VidModeValidateModeLine.3.gz


%changelog
# let's skip this for now
