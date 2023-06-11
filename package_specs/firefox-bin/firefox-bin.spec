Name:       firefox-bin
Version:    115.0b3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    firefox-%{version}.tar.bz2
Source1:    firefox.desktop

AutoProv: no
AutoReq: no

Provides: firefox = %{version}
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
* Sun Jun 11 2023 Chris Statzer <chris.statzer@gmail.com> 115.0b3
- version bump

* Mon Nov 30 2020 Chris Statzer <chris.statzer@qq.com> 83.0
- version bump

* Fri Sep 11 2020 Chris Statzer <chris.statzer@qq.com> 80.0.1
- version bump

* Sat Aug 29 2020 Chris Statzer <chris.statzer@qq.com> 80.0
- version bump

* Wed Aug 19 2020 Chris Statzer <chris.statzer@qq.com> 79.0
- version bump

* Sat Jul 18 2020 Chris Statzer <chris.statzer@qq.com> 78.0.2
- version bump

