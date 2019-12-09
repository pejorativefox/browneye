Name:       unzip
Version:    60
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}%{version}.tar.gz
Patch:      unzip-6.0-consolidated_fixes-1.patch

%description
TODO

%prep
%setup -a 0 -n unzip60

%build
make -f unix/Makefile generic_gcc

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
cp unzip %{buildroot}/usr/bin

%files
/usr/bin/unzip


%changelog
# let's skip this for now

