Name:       libXaw
Version:    1.0.13
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
/usr/include/X11/Xaw/AllWidgets.h
/usr/include/X11/Xaw/AsciiSink.h
/usr/include/X11/Xaw/AsciiSinkP.h
/usr/include/X11/Xaw/AsciiSrc.h
/usr/include/X11/Xaw/AsciiSrcP.h
/usr/include/X11/Xaw/AsciiText.h
/usr/include/X11/Xaw/AsciiTextP.h
/usr/include/X11/Xaw/Box.h
/usr/include/X11/Xaw/BoxP.h
/usr/include/X11/Xaw/Cardinals.h
/usr/include/X11/Xaw/Command.h
/usr/include/X11/Xaw/CommandP.h
/usr/include/X11/Xaw/Dialog.h
/usr/include/X11/Xaw/DialogP.h
/usr/include/X11/Xaw/Form.h
/usr/include/X11/Xaw/FormP.h
/usr/include/X11/Xaw/Grip.h
/usr/include/X11/Xaw/GripP.h
/usr/include/X11/Xaw/Label.h
/usr/include/X11/Xaw/LabelP.h
/usr/include/X11/Xaw/List.h
/usr/include/X11/Xaw/ListP.h
/usr/include/X11/Xaw/MenuButtoP.h
/usr/include/X11/Xaw/MenuButton.h
/usr/include/X11/Xaw/MultiSink.h
/usr/include/X11/Xaw/MultiSinkP.h
/usr/include/X11/Xaw/MultiSrc.h
/usr/include/X11/Xaw/MultiSrcP.h
/usr/include/X11/Xaw/Paned.h
/usr/include/X11/Xaw/PanedP.h
/usr/include/X11/Xaw/Panner.h
/usr/include/X11/Xaw/PannerP.h
/usr/include/X11/Xaw/Porthole.h
/usr/include/X11/Xaw/PortholeP.h
/usr/include/X11/Xaw/Repeater.h
/usr/include/X11/Xaw/RepeaterP.h
/usr/include/X11/Xaw/Reports.h
/usr/include/X11/Xaw/Scrollbar.h
/usr/include/X11/Xaw/ScrollbarP.h
/usr/include/X11/Xaw/Simple.h
/usr/include/X11/Xaw/SimpleMenP.h
/usr/include/X11/Xaw/SimpleMenu.h
/usr/include/X11/Xaw/SimpleP.h
/usr/include/X11/Xaw/Sme.h
/usr/include/X11/Xaw/SmeBSB.h
/usr/include/X11/Xaw/SmeBSBP.h
/usr/include/X11/Xaw/SmeLine.h
/usr/include/X11/Xaw/SmeLineP.h
/usr/include/X11/Xaw/SmeP.h
/usr/include/X11/Xaw/StripCharP.h
/usr/include/X11/Xaw/StripChart.h
/usr/include/X11/Xaw/Template.c
/usr/include/X11/Xaw/Template.h
/usr/include/X11/Xaw/TemplateP.h
/usr/include/X11/Xaw/Text.h
/usr/include/X11/Xaw/TextP.h
/usr/include/X11/Xaw/TextSink.h
/usr/include/X11/Xaw/TextSinkP.h
/usr/include/X11/Xaw/TextSrc.h
/usr/include/X11/Xaw/TextSrcP.h
/usr/include/X11/Xaw/Tip.h
/usr/include/X11/Xaw/TipP.h
/usr/include/X11/Xaw/Toggle.h
/usr/include/X11/Xaw/ToggleP.h
/usr/include/X11/Xaw/Tree.h
/usr/include/X11/Xaw/TreeP.h
/usr/include/X11/Xaw/VendorEP.h
/usr/include/X11/Xaw/Viewport.h
/usr/include/X11/Xaw/ViewportP.h
/usr/include/X11/Xaw/XawImP.h
/usr/include/X11/Xaw/XawInit.h
/usr/lib64/libXaw.so
/usr/lib64/libXaw.so.6
/usr/lib64/libXaw.so.7
/usr/lib64/libXaw6.a
/usr/lib64/libXaw6.so
/usr/lib64/libXaw6.so.6
/usr/lib64/libXaw6.so.6.0.1
/usr/lib64/libXaw7.a
/usr/lib64/libXaw7.so
/usr/lib64/libXaw7.so.7
/usr/lib64/libXaw7.so.7.0.0
/usr/lib64/pkgconfig/xaw6.pc
/usr/lib64/pkgconfig/xaw7.pc
/usr/share/doc/libXaw/AsciiSink.xml
/usr/share/doc/libXaw/AsciiSource.xml
/usr/share/doc/libXaw/AsciiText.xml
/usr/share/doc/libXaw/Box.xml
/usr/share/doc/libXaw/CH1.xml
/usr/share/doc/libXaw/CH2.xml
/usr/share/doc/libXaw/CH3.xml
/usr/share/doc/libXaw/CH4.xml
/usr/share/doc/libXaw/CH5.xml
/usr/share/doc/libXaw/CH6.xml
/usr/share/doc/libXaw/CH7.xml
/usr/share/doc/libXaw/Command.xml
/usr/share/doc/libXaw/Dialog.xml
/usr/share/doc/libXaw/Form.xml
/usr/share/doc/libXaw/Grip.xml
/usr/share/doc/libXaw/Label.xml
/usr/share/doc/libXaw/List.xml
/usr/share/doc/libXaw/MenuButton.xml
/usr/share/doc/libXaw/Paned.xml
/usr/share/doc/libXaw/Panner.xml
/usr/share/doc/libXaw/Porthole.xml
/usr/share/doc/libXaw/Repeater.xml
/usr/share/doc/libXaw/Scrollbar.xml
/usr/share/doc/libXaw/Simple.xml
/usr/share/doc/libXaw/SimpleMenu.xml
/usr/share/doc/libXaw/Sme.xml
/usr/share/doc/libXaw/SmeBSB.xml
/usr/share/doc/libXaw/SmeLine.xml
/usr/share/doc/libXaw/StripChart.xml
/usr/share/doc/libXaw/TPage_Credits.xml
/usr/share/doc/libXaw/Template.xml
/usr/share/doc/libXaw/Template_private_header_file.xml
/usr/share/doc/libXaw/Template_public_header_file.xml
/usr/share/doc/libXaw/Template_widget_source_file.xml
/usr/share/doc/libXaw/Text.xml
/usr/share/doc/libXaw/TextActions.xml
/usr/share/doc/libXaw/TextActions_default_translation_bindings.xml
/usr/share/doc/libXaw/TextActions_text_widget_actions.xml
/usr/share/doc/libXaw/TextCustom.xml
/usr/share/doc/libXaw/TextFuncs.xml
/usr/share/doc/libXaw/TextSink.xml
/usr/share/doc/libXaw/TextSource.xml
/usr/share/doc/libXaw/Toggle.xml
/usr/share/doc/libXaw/Tree.xml
/usr/share/doc/libXaw/Viewport.xml
/usr/share/doc/libXaw/libXaw.xml
/usr/share/man/man3/Xaw.3.gz


%changelog
# let's skip this for now
