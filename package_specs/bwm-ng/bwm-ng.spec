Name:       bwm-ng
Version:    0.6.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
pushd %{name}-%{version}
./autogen.sh --prefix=/usr
%make_build
popd

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin

pushd %{name}-%{version}
cp src/bwm-ng %{buildroot}/usr/bin
popd

%files
/usr/bin/bwm-ng

%changelog
# let's skip this for now
