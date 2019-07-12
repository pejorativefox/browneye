Name:       libXv
Version:    1.0.11
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
/usr/include/X11/extensions/Xvlib.h
/usr/lib64/libXv.a
/usr/lib64/libXv.la
/usr/lib64/libXv.so
/usr/lib64/libXv.so.1
/usr/lib64/libXv.so.1.0.0
/usr/lib64/pkgconfig/xv.pc
/usr/share/man/man3/Xv.3.gz
/usr/share/man/man3/XvCreateImage.3.gz
/usr/share/man/man3/XvFreeAdaptorInfo.3.gz
/usr/share/man/man3/XvFreeEncodingInfo.3.gz
/usr/share/man/man3/XvGetPortAttribute.3.gz
/usr/share/man/man3/XvGetStill.3.gz
/usr/share/man/man3/XvGetVideo.3.gz
/usr/share/man/man3/XvGrabPort.3.gz
/usr/share/man/man3/XvListImageFormats.3.gz
/usr/share/man/man3/XvPortNotify.3.gz
/usr/share/man/man3/XvPutImage.3.gz
/usr/share/man/man3/XvPutStill.3.gz
/usr/share/man/man3/XvPutVideo.3.gz
/usr/share/man/man3/XvQueryAdaptors.3.gz
/usr/share/man/man3/XvQueryBestSize.3.gz
/usr/share/man/man3/XvQueryEncodings.3.gz
/usr/share/man/man3/XvQueryExtension.3.gz
/usr/share/man/man3/XvQueryPortAttributes.3.gz
/usr/share/man/man3/XvSelectPortNotify.3.gz
/usr/share/man/man3/XvSelectVideoNotify.3.gz
/usr/share/man/man3/XvSetPortAttribute.3.gz
/usr/share/man/man3/XvShmCreateImage.3.gz
/usr/share/man/man3/XvShmPutImage.3.gz
/usr/share/man/man3/XvStopVideo.3.gz
/usr/share/man/man3/XvUngrabPort.3.gz
/usr/share/man/man3/XvVideoNotify.3.gz

%changelog
# let's skip this for now
