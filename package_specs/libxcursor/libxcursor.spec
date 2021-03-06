Name:       libXcursor
Version:    1.1.15
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
/usr/include/X11/Xcursor/Xcursor.h
/usr/lib64/libXcursor.a
/usr/lib64/libXcursor.la
/usr/lib64/libXcursor.so
/usr/lib64/libXcursor.so.1
/usr/lib64/libXcursor.so.1.0.2
/usr/lib64/pkgconfig/xcursor.pc
/usr/share/man/man3/Xcursor.3.gz
/usr/share/man/man3/XcursorCursorsCreate.3.gz
/usr/share/man/man3/XcursorCursorsDestroy.3.gz
/usr/share/man/man3/XcursorFilenameLoad.3.gz
/usr/share/man/man3/XcursorFilenameLoadAllImages.3.gz
/usr/share/man/man3/XcursorFilenameLoadCursor.3.gz
/usr/share/man/man3/XcursorFilenameLoadImage.3.gz
/usr/share/man/man3/XcursorFilenameLoadImages.3.gz
/usr/share/man/man3/XcursorFilenameSave.3.gz
/usr/share/man/man3/XcursorFilenameSaveImages.3.gz
/usr/share/man/man3/XcursorGetDefaultSize.3.gz
/usr/share/man/man3/XcursorGetTheme.3.gz
/usr/share/man/man3/XcursorImageCreate.3.gz
/usr/share/man/man3/XcursorImageDestroy.3.gz
/usr/share/man/man3/XcursorImagesCreate.3.gz
/usr/share/man/man3/XcursorImagesDestroy.3.gz
/usr/share/man/man3/XcursorLibraryLoadCursor.3.gz
/usr/share/man/man3/XcursorLibraryLoadCursors.3.gz
/usr/share/man/man3/XcursorLibraryLoadImage.3.gz
/usr/share/man/man3/XcursorLibraryLoadImages.3.gz
/usr/share/man/man3/XcursorSetDefaultSize.3.gz
/usr/share/man/man3/XcursorSetTheme.3.gz
/usr/share/man/man3/XcursorShapeLoadCursor.3.gz
/usr/share/man/man3/XcursorShapeLoadCursors.3.gz
/usr/share/man/man3/XcursorShapeLoadImage.3.gz
/usr/share/man/man3/XcursorShapeLoadImages.3.gz
/usr/share/man/man3/XcursorSupportsARGB.3.gz
/usr/share/man/man3/XcursorXcFileLoad.3.gz
/usr/share/man/man3/XcursorXcFileLoadAllImages.3.gz
/usr/share/man/man3/XcursorXcFileLoadImage.3.gz
/usr/share/man/man3/XcursorXcFileLoadImages.3.gz
/usr/share/man/man3/XcursorXcFileSave.3.gz

%changelog
# let's skip this for now
