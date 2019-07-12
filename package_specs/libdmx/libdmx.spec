Name:       libdmx
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
/usr/include/X11/extensions/dmxext.h
/usr/lib64/libdmx.a
/usr/lib64/libdmx.la
/usr/lib64/libdmx.so
/usr/lib64/libdmx.so.1
/usr/lib64/libdmx.so.1.0.0
/usr/lib64/pkgconfig/dmx.pc
/usr/share/man/man3/DMX.3.gz
/usr/share/man/man3/DMXAddInput.3.gz
/usr/share/man/man3/DMXAddScreen.3.gz
/usr/share/man/man3/DMXChangeDesktopAttributes.3.gz
/usr/share/man/man3/DMXChangeScreensAttributes.3.gz
/usr/share/man/man3/DMXForceWindowCreation.3.gz
/usr/share/man/man3/DMXGetDesktopAttributes.3.gz
/usr/share/man/man3/DMXGetInputAttributes.3.gz
/usr/share/man/man3/DMXGetInputCount.3.gz
/usr/share/man/man3/DMXGetScreenAttributes.3.gz
/usr/share/man/man3/DMXGetScreenCount.3.gz
/usr/share/man/man3/DMXGetWindowAttributes.3.gz
/usr/share/man/man3/DMXQueryExtension.3.gz
/usr/share/man/man3/DMXQueryVersion.3.gz
/usr/share/man/man3/DMXRemoveInput.3.gz
/usr/share/man/man3/DMXRemoveScreen.3.gz
/usr/share/man/man3/DMXSync.3.gz


%changelog
# let's skip this for now
