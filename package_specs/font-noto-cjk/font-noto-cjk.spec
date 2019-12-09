# https://dspk.xyz/noto-cjk-2.001.tar.gz
Name:       font-noto-cjk
Version:    2.001
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    noto-cjk-%{version}.tar.gz



%description
TODO

%prep
%setup -a 0 -n noto-cjk-2.001

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/share/fonts/noto-cjk
cp *.ttc %{buildroot}/usr/share/fonts/noto-cjk/

%files
/usr/share/fonts/noto-cjk/*

%changelog
# let's skip this for now

