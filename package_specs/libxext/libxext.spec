Name:       libXext
Version:    1.3.3
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
%configure ICE_LIBS=-lpthread
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/MITMisc.h
/usr/include/X11/extensions/XEVI.h
/usr/include/X11/extensions/XLbx.h
/usr/include/X11/extensions/XShm.h
/usr/include/X11/extensions/Xag.h
/usr/include/X11/extensions/Xcup.h
/usr/include/X11/extensions/Xdbe.h
/usr/include/X11/extensions/Xext.h
/usr/include/X11/extensions/Xge.h
/usr/include/X11/extensions/dpms.h
/usr/include/X11/extensions/extutil.h
/usr/include/X11/extensions/multibuf.h
/usr/include/X11/extensions/security.h
/usr/include/X11/extensions/shape.h
/usr/include/X11/extensions/sync.h
/usr/include/X11/extensions/xtestext1.h
/usr/lib64/libXext.a
/usr/lib64/libXext.so
/usr/lib64/libXext.so.6
/usr/lib64/libXext.so.6.4.0
/usr/lib64/pkgconfig/xext.pc
/usr/share/doc/libXext/dbelib.xml
/usr/share/doc/libXext/dpmslib.xml
/usr/share/doc/libXext/shapelib.xml
/usr/share/doc/libXext/synclib.xml
/usr/share/doc/libXext/xtest1.xml
/usr/share/man/man3/DBE.3.gz
/usr/share/man/man3/DPMSCapable.3.gz
/usr/share/man/man3/DPMSDisable.3.gz
/usr/share/man/man3/DPMSEnable.3.gz
/usr/share/man/man3/DPMSForceLevel.3.gz
/usr/share/man/man3/DPMSGetTimeouts.3.gz
/usr/share/man/man3/DPMSGetVersion.3.gz
/usr/share/man/man3/DPMSInfo.3.gz
/usr/share/man/man3/DPMSQueryExtension.3.gz
/usr/share/man/man3/DPMSSetTimeouts.3.gz
/usr/share/man/man3/XShape.3.gz
/usr/share/man/man3/XShapeCombineMask.3.gz
/usr/share/man/man3/XShapeCombineRectangles.3.gz
/usr/share/man/man3/XShapeCombineRegion.3.gz
/usr/share/man/man3/XShapeCombineShape.3.gz
/usr/share/man/man3/XShapeGetRectangles.3.gz
/usr/share/man/man3/XShapeInputSelected.3.gz
/usr/share/man/man3/XShapeOffsetShape.3.gz
/usr/share/man/man3/XShapeQueryExtension.3.gz
/usr/share/man/man3/XShapeQueryExtents.3.gz
/usr/share/man/man3/XShapeQueryVersion.3.gz
/usr/share/man/man3/XShapeSelectInput.3.gz
/usr/share/man/man3/XShm.3.gz
/usr/share/man/man3/XShmAttach.3.gz
/usr/share/man/man3/XShmCreateImage.3.gz
/usr/share/man/man3/XShmCreatePixmap.3.gz
/usr/share/man/man3/XShmDetach.3.gz
/usr/share/man/man3/XShmGetEventBase.3.gz
/usr/share/man/man3/XShmGetImage.3.gz
/usr/share/man/man3/XShmPixmapFormat.3.gz
/usr/share/man/man3/XShmPutImage.3.gz
/usr/share/man/man3/XShmQueryExtension.3.gz
/usr/share/man/man3/XShmQueryVersion.3.gz
/usr/share/man/man3/XcupGetReservedColormapEntries.3.gz
/usr/share/man/man3/XcupQueryVersion.3.gz
/usr/share/man/man3/XcupStoreColors.3.gz
/usr/share/man/man3/XdbeAllocateBackBufferName.3.gz
/usr/share/man/man3/XdbeBeginIdiom.3.gz
/usr/share/man/man3/XdbeDeallocateBackBufferName.3.gz
/usr/share/man/man3/XdbeEndIdiom.3.gz
/usr/share/man/man3/XdbeFreeVisualInfo.3.gz
/usr/share/man/man3/XdbeGetBackBufferAttributes.3.gz
/usr/share/man/man3/XdbeGetVisualInfo.3.gz
/usr/share/man/man3/XdbeQueryExtension.3.gz
/usr/share/man/man3/XdbeSwapBuffers.3.gz
/usr/share/man/man3/Xevi.3.gz
/usr/share/man/man3/XeviGetVisualInfo.3.gz
/usr/share/man/man3/XeviQueryExtension.3.gz
/usr/share/man/man3/XeviQueryVersion.3.gz
/usr/share/man/man3/Xmbuf.3.gz
/usr/share/man/man3/XmbufChangeBufferAttributes.3.gz
/usr/share/man/man3/XmbufChangeWindowAttributes.3.gz
/usr/share/man/man3/XmbufCreateBuffers.3.gz
/usr/share/man/man3/XmbufCreateStereoWindow.3.gz
/usr/share/man/man3/XmbufDestroyBuffers.3.gz
/usr/share/man/man3/XmbufDisplayBuffers.3.gz
/usr/share/man/man3/XmbufGetBufferAttributes.3.gz
/usr/share/man/man3/XmbufGetScreenInfo.3.gz
/usr/share/man/man3/XmbufGetVersion.3.gz
/usr/share/man/man3/XmbufGetWindowAttributes.3.gz
/usr/share/man/man3/XmbufQueryExtension.3.gz


%changelog
# let's skip this for now
