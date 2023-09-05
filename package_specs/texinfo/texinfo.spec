Name:       texinfo
Version:    7.0.3
Release:    1
Summary:    GNU texinfo utility
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

AutoReq: no

Requires: libc.so.6()(64bit), libncursesw.so.6()(64bit), perl >= 0:5.004

%description
The Texinfo package contains programs for reading, writing, and converting info pages. 

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/info
/usr/bin/install-info
/usr/bin/makeinfo
/usr/bin/pdftexi2dvi
/usr/bin/pod2texi
/usr/bin/texi2any
/usr/bin/texi2dvi
/usr/bin/texi2pdf
/usr/bin/texindex
/usr/lib64/texinfo/MiscXS.so
/usr/lib64/texinfo/Parsetexi.so
/usr/lib64/texinfo/XSParagraph.so
/usr/share/info/
/usr/share/texinfo/
/usr/share/locale/
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 7.0.3-1
- Version bump
