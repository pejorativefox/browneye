Name:       chromium-bin
Version:    1159763
Release:    1
Summary:    Chromium Web Browser
License:    Custom
Prefix:     /usr
Source0:    chrome-linux.zip
Source1:    chromium.desktop

#AutoProv: no
AutoReq: no

Requires: ld-linux-x86-64.so.2()(64bit), libX11.so.6()(64bit), libc.so.6()(64bit), libstdc++.so.6()(64bit)

%description
Chromium Web Browser

%prep
%setup -n chrome-linux

%build

%install    
rm -rf %{buildroot}
#pushd chrome-linux
mkdir -pv %{buildroot}/opt/chromium
ls
cp -r * %{buildroot}/opt/chromium
#popd
mkdir -pv %{buildroot}/share/applications
cp %{SOURCE1} %{buildroot}/share/applications

%files
/opt/chromium
/share/applications/chromium.desktop

%changelog
* Tue Jun 20 2023 Chris Statzer <chris.statzer@gmail.com> 1159763
- version bump

* Wed Jan 13 2021 Chris Statzer <chris.statzer@qq.com> 842801
- version bump

