Name:       libXScrnSaver
Version:    1.2.3
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
/usr/include/X11/extensions/scrnsaver.h
/usr/lib64/libXss.a
/usr/lib64/libXss.la
/usr/lib64/libXss.so
/usr/lib64/libXss.so.1
/usr/lib64/libXss.so.1.0.0
/usr/lib64/pkgconfig/xscrnsaver.pc
/usr/share/man/man3/XScreenSaverAllocInfo.3.gz
/usr/share/man/man3/XScreenSaverGetRegistered.3.gz
/usr/share/man/man3/XScreenSaverQueryExtension.3.gz
/usr/share/man/man3/XScreenSaverQueryInfo.3.gz
/usr/share/man/man3/XScreenSaverQueryVersion.3.gz
/usr/share/man/man3/XScreenSaverRegister.3.gz
/usr/share/man/man3/XScreenSaverSelectInput.3.gz
/usr/share/man/man3/XScreenSaverSetAttributes.3.gz
/usr/share/man/man3/XScreenSaverSuspend.3.gz
/usr/share/man/man3/XScreenSaverUnregister.3.gz
/usr/share/man/man3/XScreenSaverUnsetAttributes.3.gz
/usr/share/man/man3/Xss.3.gz


%changelog
# let's skip this for now
