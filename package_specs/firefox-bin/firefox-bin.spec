Name:       firefox-bin
Version:    71.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    firefox-%{version}.tar.bz2


%description
TODO

%prep
rm -rf firefox-bin
mkdir firefox-bin
pushd firefox-bin
tar xf %{SOURCE0}
popd
%build

%install    
rm -rf %{buildroot}
pushd firefox-bin
mkdir -pv %{buildroot}/opt
cp -r firefox %{buildroot}/opt
popd

%files
/opt/firefox/*

%changelog
# let's skip this for now

