Name:       transgui-bin
Version:    5.18.0
Release:    1
Summary:    A feature rich cross platform Transmission BitTorrent client. 
License:    GPL
Source0:    transgui-%{version}-x86_64-Linux.txz
Source1:    transgui.desktop
Prefix:     /usr

%description
Faster and has more functionality than the built-in web GUI. 

%prep
%setup -c transgui-bin-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/share/transgui
cp -r lang transgui.png %{buildroot}/share/transgui
mkdir -pv %{buildroot}/bin
cp transgui %{buildroot}/bin
mkdir -pv %{buildroot}/share/applications
cp %{SOURCE1} %{buildroot}/share/applications/

%files
/bin/transgui
/share/transgui/lang/
/share/transgui/transgui.png
/share/applications/transgui.desktop

%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 5.18.0
- Initial RPM

