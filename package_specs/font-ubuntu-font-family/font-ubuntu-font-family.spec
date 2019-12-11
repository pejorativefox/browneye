Name:       font-ubuntu-font-family
Version:    0.83
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    ubuntu-font-family-sources_%{version}.orig.tar.gz



%description
TODO

%prep
%setup -n ubuntu-font-family-sources-%{version}

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/share/fonts/ubuntu-font-family
cp *.ttf %{buildroot}/usr/share/fonts/ubuntu-font-family

%post
fc-cache -f -v

%files
/usr/share/fonts/ubuntu-font-family/*

%changelog
# let's skip this for now

