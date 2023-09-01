Name:       libXcomposite
Version:    0.4.4
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
/usr/include/X11/extensions/Xcomposite.h
/usr/lib64/libXcomposite.a
/usr/lib64/libXcomposite.so
/usr/lib64/libXcomposite.so.1
/usr/lib64/libXcomposite.so.1.0.0
/usr/lib64/pkgconfig/xcomposite.pc
/usr/share/man/man3/XCompositeCreateRegionFromBorderClip.3.gz
/usr/share/man/man3/XCompositeGetOverlayWindow.3.gz
/usr/share/man/man3/XCompositeNameWindowPixmap.3.gz
/usr/share/man/man3/XCompositeQueryExtension.3.gz
/usr/share/man/man3/XCompositeQueryVersion.3.gz
/usr/share/man/man3/XCompositeRedirectSubwindows.3.gz
/usr/share/man/man3/XCompositeRedirectWindow.3.gz
/usr/share/man/man3/XCompositeReleaseOverlayWindow.3.gz
/usr/share/man/man3/XCompositeUnredirectSubwindows.3.gz
/usr/share/man/man3/XCompositeUnredirectWindow.3.gz
/usr/share/man/man3/XCompositeVersion.3.gz
/usr/share/man/man3/Xcomposite.3.gz

%changelog
# let's skip this for now
