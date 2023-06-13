Name:       chromium-bin
Version:    842801
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    chrome-linux.zip
Source1:    chromium.desktop

#AutoProv: no
AutoReq: no

#Provides: firefox = %{version}
Requires: ld-linux-x86-64.so.2()(64bit), libX11.so.6()(64bit), libc.so.6()(64bit), libstdc++.so.6()(64bit)
%description


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
* Wed Jan 13 2021 Chris Statzer <chris.statzer@qq.com> 842801
- version bump

