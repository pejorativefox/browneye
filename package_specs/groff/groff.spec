Name:       groff
Version:    1.23.0
Release:    1
Summary:    GNU typesetting system
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: libICE.so.6()(64bit), libSM.so.6()(64bit), libX11.so.6()(64bit), libXaw.so.7()(64bit), libXmu.so.6()(64bit), libXt.so.6()(64bit), libc.so.6()(64bit), libgcc_s.so.1()(64bit), libm.so.6()(64bit), libstdc++.so.6()(64bit), perl >= 0:5.004

%description
groff (GNU roff) is a typesetting system that reads plain text input files that include formatting commands to produce output in PostScript, PDF, HTML, or DVI formats or for display to a terminal. 

%prep
%setup -q

%build
export PAGE=letter
%configure 
%make_build
unset PAGE

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files -f ../../SOURCES/groff.filelist

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump
