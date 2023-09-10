Name:       libxt
Version:    1.3.0
Release:    1
Summary:    X Toolkit Intrinsics library
License:    GPL3
Prefix:     /usr
Source0:    libXt-%{version}.tar.xz

BuildRequires: libsm

%description
X Toolkit Intrinsics library

%prep
%setup -q -n libXt-%{version}


%build
%configure --with-appdefaultdir=/etc/X11/app-defaults
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/CallbackI.h
/usr/include/X11/Composite.h
/usr/include/X11/CompositeP.h
/usr/include/X11/ConstrainP.h
/usr/include/X11/Constraint.h
/usr/include/X11/ConvertI.h
/usr/include/X11/Core.h
/usr/include/X11/CoreP.h
/usr/include/X11/CreateI.h
/usr/include/X11/EventI.h
/usr/include/X11/HookObjI.h
/usr/include/X11/InitialI.h
/usr/include/X11/Intrinsic.h
/usr/include/X11/IntrinsicI.h
/usr/include/X11/IntrinsicP.h
/usr/include/X11/Object.h
/usr/include/X11/ObjectP.h
/usr/include/X11/PassivGraI.h
/usr/include/X11/RectObj.h
/usr/include/X11/RectObjP.h
/usr/include/X11/ResConfigP.h
/usr/include/X11/ResourceI.h
/usr/include/X11/SelectionI.h
/usr/include/X11/Shell.h
/usr/include/X11/ShellI.h
/usr/include/X11/ShellP.h
/usr/include/X11/StringDefs.h
/usr/include/X11/ThreadsI.h
/usr/include/X11/TranslateI.h
/usr/include/X11/VarargsI.h
/usr/include/X11/Vendor.h
/usr/include/X11/VendorP.h
/usr/include/X11/Xtos.h
/usr/lib64/libXt.a
/usr/lib64/libXt.so
/usr/lib64/libXt.so.6
/usr/lib64/libXt.so.6.0.0
/usr/lib64/pkgconfig/xt.pc
/usr/share/doc/
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.3.0-1
- Version bump
