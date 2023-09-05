Name:       sed
Version:    4.9
Release:    1
Summary:    The sed stream editor
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
sed (stream editor) is a non-interactive command-line text editor. 

%prep
%setup -q

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*


%files
/usr/bin/sed
/usr/share/info/sed.info.gz
/usr/share/locale/
/usr/share/man/man1/sed.1.gz

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump
