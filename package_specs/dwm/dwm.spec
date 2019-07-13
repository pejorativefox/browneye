Name:       dwm
Version:    6.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
make config.h

sed -i -e 's/"st"/"xterm"/g' config.h
sed -i -e 's/#define MODKEY Mod1Mask/#define MODKEY Mod4Mask/g' config.h

make

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
cp dwm %{buildroot}/usr/bin/
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/dwm

%changelog
# let's skip this for now

