Name:       kdevelop-bin
Version:    5.5.2
Release:    1
Summary:    Kdevelop dev platform
License:    GPL
Source0:    KDevelop-%{version}-x86_64.AppImage
Source1:    kdevelop-bin.desktop
Prefix:     /usr

%description
KDevelop - A cross-platform IDE for C, C++, Python, QML/JavaScript and PHP

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp %{SOURCE0} %{buildroot}/usr/bin/kdevelop 

mkdir -pv %{buildroot}/share/applications
cp %{SOURCE1} %{buildroot}/share/applications


%files
/share/applications/kdevelop-bin.desktop
/usr/bin/kdevelop

%changelog
* Sun Aug 30 2020 Chris Statzer <chris.statzer@qq.com> 5.5.2
- Initial RPM

