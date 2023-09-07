Name:       groff
Version:    1.23.0
Release:    1
Summary:    GNU typesetting system
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

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
