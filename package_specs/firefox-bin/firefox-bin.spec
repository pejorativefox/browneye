Name:       firefox-bin
Version:    76.0.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    firefox-%{version}.tar.bz2
Source1:    firefox.desktop

AutoProv: no
AutoReq: no

Provides: firefox = 76.0
Requires: ld-linux-x86-64.so.2()(64bit), libX11.so.6()(64bit), libc.so.6()(64bit), libstdc++.so.6()(64bit)
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
mkdir -pv %{buildroot}/share/applications
cp %{SOURCE1} %{buildroot}/share/applications

%files
/opt/firefox/*
/share/applications/firefox.desktop

%changelog
# let's skip this for now

