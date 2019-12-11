Name:       font-ttf-unifont
Version:    12.1.04
Release:    1
Summary:    GNU Unifont.
License:    GPL3
Prefix:     /usr
Source0:    ttf-unifont-%{version}.tar.gz

%description
GNU Unifont

%prep
%setup -n ttf-unifont-%{version}

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/share/fonts/unifont
cp *.ttf %{buildroot}/usr/share/fonts/unifont/

%files
/usr/share/fonts/unifont/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM
