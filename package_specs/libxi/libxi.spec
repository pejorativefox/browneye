Name:       libXi
Version:    1.7.9
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
/usr/include/X11/extensions/XInput.h
/usr/include/X11/extensions/XInput2.h
/usr/lib64/libXi.a
/usr/lib64/libXi.so
/usr/lib64/libXi.so.6
/usr/lib64/libXi.so.6.1.0
/usr/lib64/pkgconfig/xi.pc
/usr/share/doc/libXi/encoding.xml
/usr/share/doc/libXi/inputlib.xml
/usr/share/doc/libXi/library.xml
/usr/share/man/man3/XAllowDeviceEvents.3.gz
/usr/share/man/man3/XChangeDeviceControl.3.gz
/usr/share/man/man3/XChangeDeviceDontPropagateList.3.gz
/usr/share/man/man3/XChangeDeviceKeyMapping.3.gz
/usr/share/man/man3/XChangeDeviceProperty.3.gz
/usr/share/man/man3/XChangeFeedbackControl.3.gz
/usr/share/man/man3/XChangeKeyboardDevice.3.gz
/usr/share/man/man3/XChangePointerDevice.3.gz
/usr/share/man/man3/XCloseDevice.3.gz
/usr/share/man/man3/XDeleteDeviceProperty.3.gz
/usr/share/man/man3/XDeviceBell.3.gz
/usr/share/man/man3/XDeviceTimeCoord.3.gz
/usr/share/man/man3/XFreeDeviceList.3.gz
/usr/share/man/man3/XGetDeviceButtonMapping.3.gz
/usr/share/man/man3/XGetDeviceControl.3.gz
/usr/share/man/man3/XGetDeviceDontPropagateList.3.gz
/usr/share/man/man3/XGetDeviceFocus.3.gz
/usr/share/man/man3/XGetDeviceKeyMapping.3.gz
/usr/share/man/man3/XGetDeviceModifierMapping.3.gz
/usr/share/man/man3/XGetDeviceMotionEvents.3.gz
/usr/share/man/man3/XGetDeviceProperty.3.gz
/usr/share/man/man3/XGetExtensionVersion.3.gz
/usr/share/man/man3/XGetFeedbackControl.3.gz
/usr/share/man/man3/XGetSelectedExtensionEvents.3.gz
/usr/share/man/man3/XGrabDevice.3.gz
/usr/share/man/man3/XGrabDeviceButton.3.gz
/usr/share/man/man3/XGrabDeviceKey.3.gz
/usr/share/man/man3/XIBarrierReleasePointer.3.gz
/usr/share/man/man3/XIBarrierReleasePointers.3.gz
/usr/share/man/man3/XIChangeHierarchy.3.gz
/usr/share/man/man3/XIChangeProperty.3.gz
/usr/share/man/man3/XIDefineCursor.3.gz
/usr/share/man/man3/XIDeleteProperty.3.gz
/usr/share/man/man3/XIFreeDeviceInfo.3.gz
/usr/share/man/man3/XIGetClientPointer.3.gz
/usr/share/man/man3/XIGetFocus.3.gz
/usr/share/man/man3/XIGetProperty.3.gz
/usr/share/man/man3/XIGetSelectedEvents.3.gz
/usr/share/man/man3/XIGrabButton.3.gz
/usr/share/man/man3/XIGrabDevice.3.gz
/usr/share/man/man3/XIGrabEnter.3.gz
/usr/share/man/man3/XIGrabFocusIn.3.gz
/usr/share/man/man3/XIGrabKeycode.3.gz
/usr/share/man/man3/XIGrabTouchBegin.3.gz
/usr/share/man/man3/XIListProperties.3.gz
/usr/share/man/man3/XIQueryDevice.3.gz
/usr/share/man/man3/XIQueryPointer.3.gz
/usr/share/man/man3/XIQueryVersion.3.gz
/usr/share/man/man3/XISelectEvents.3.gz
/usr/share/man/man3/XISetClientPointer.3.gz
/usr/share/man/man3/XISetFocus.3.gz
/usr/share/man/man3/XIUndefineCursor.3.gz
/usr/share/man/man3/XIUngrabButton.3.gz
/usr/share/man/man3/XIUngrabDevice.3.gz
/usr/share/man/man3/XIUngrabEnter.3.gz
/usr/share/man/man3/XIUngrabFocusIn.3.gz
/usr/share/man/man3/XIUngrabKeycode.3.gz
/usr/share/man/man3/XIUngrabTouchBegin.3.gz
/usr/share/man/man3/XIWarpPointer.3.gz
/usr/share/man/man3/XListDeviceProperties.3.gz
/usr/share/man/man3/XListInputDevices.3.gz
/usr/share/man/man3/XOpenDevice.3.gz
/usr/share/man/man3/XQueryDeviceState.3.gz
/usr/share/man/man3/XSelectExtensionEvent.3.gz
/usr/share/man/man3/XSendExtensionEvent.3.gz
/usr/share/man/man3/XSetDeviceButtonMapping.3.gz
/usr/share/man/man3/XSetDeviceFocus.3.gz
/usr/share/man/man3/XSetDeviceMode.3.gz
/usr/share/man/man3/XSetDeviceModifierMapping.3.gz
/usr/share/man/man3/XSetDeviceValuators.3.gz
/usr/share/man/man3/XUngrabDevice.3.gz
/usr/share/man/man3/XUngrabDeviceButton.3.gz
/usr/share/man/man3/XUngrabDeviceKey.3.gz


%changelog
# let's skip this for now
