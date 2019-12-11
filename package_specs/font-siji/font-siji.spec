Name:       font-siji
Version:    0.1
Release:    1
Summary:    An iconic bitmap font based on Stlarch with additional glyphs.
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

%description
An iconic bitmap font based on Stlarch with additional glyphs.

%prep
%setup 

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/share/fonts/siji
cp *.pcf %{buildroot}/usr/share/fonts/siji/

%files
/usr/share/fonts/siji/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.1
- Initial RPM
