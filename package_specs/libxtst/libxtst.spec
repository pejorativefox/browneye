Name:       libXtst
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
/usr/include/X11/extensions/XTest.h
/usr/include/X11/extensions/record.h
/usr/lib64/libXtst.a
/usr/lib64/libXtst.so
/usr/lib64/libXtst.so.6
/usr/lib64/libXtst.so.6.1.0
/usr/lib64/pkgconfig/xtst.pc
/usr/share/doc/libXtst/recordlib.xml
/usr/share/doc/libXtst/xtestlib.xml
/usr/share/man/man3/XTestCompareCurrentCursorWithWindow.3.gz
/usr/share/man/man3/XTestCompareCursorWithWindow.3.gz
/usr/share/man/man3/XTestDiscard.3.gz
/usr/share/man/man3/XTestFakeButtonEvent.3.gz
/usr/share/man/man3/XTestFakeKeyEvent.3.gz
/usr/share/man/man3/XTestFakeMotionEvent.3.gz
/usr/share/man/man3/XTestFakeRelativeMotionEvent.3.gz
/usr/share/man/man3/XTestGrabControl.3.gz
/usr/share/man/man3/XTestQueryExtension.3.gz
/usr/share/man/man3/XTestSetGContextOfGC.3.gz
/usr/share/man/man3/XTestSetVisualIDOfVisual.3.gz

%changelog
# let's skip this for now
