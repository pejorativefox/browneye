Name:       libXxf86dga
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
/usr/include/X11/extensions/Xxf86dga.h
/usr/include/X11/extensions/xf86dga1.h
/usr/lib64/libXxf86dga.a
/usr/lib64/libXxf86dga.la
/usr/lib64/libXxf86dga.so
/usr/lib64/libXxf86dga.so.1
/usr/lib64/libXxf86dga.so.1.0.0
/usr/lib64/pkgconfig/xxf86dga.pc
/usr/share/man/man3/XDGA.3.gz
/usr/share/man/man3/XDGAChangePixmapMode.3.gz
/usr/share/man/man3/XDGACloseFramebuffer.3.gz
/usr/share/man/man3/XDGACopyArea.3.gz
/usr/share/man/man3/XDGACopyTransparentArea.3.gz
/usr/share/man/man3/XDGACreateColormap.3.gz
/usr/share/man/man3/XDGAFillRectangle.3.gz
/usr/share/man/man3/XDGAGetViewportStatus.3.gz
/usr/share/man/man3/XDGAInstallColormap.3.gz
/usr/share/man/man3/XDGAKeyEventToXKeyEvent.3.gz
/usr/share/man/man3/XDGAOpenFramebuffer.3.gz
/usr/share/man/man3/XDGAQueryExtension.3.gz
/usr/share/man/man3/XDGAQueryModes.3.gz
/usr/share/man/man3/XDGAQueryVersion.3.gz
/usr/share/man/man3/XDGASelectInput.3.gz
/usr/share/man/man3/XDGASetClientVersion.3.gz
/usr/share/man/man3/XDGASetMode.3.gz
/usr/share/man/man3/XDGASetViewport.3.gz
/usr/share/man/man3/XDGASync.3.gz
/usr/share/man/man3/XF86DGA.3.gz
/usr/share/man/man3/XFree86-DGA.3.gz


%changelog
# let's skip this for now
