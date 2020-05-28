Name:       squashfs-tools
Version:    4.4
Release:    1
Summary:    tools to create and extract Squashfs filesystems
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
tools to create and extract Squashfs filesystems


%prep
%setup

%build
pushd squashfs-tools
%make_build
popd

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/bin/
pushd squashfs-tools
cp mksquashfs %{buildroot}/bin/
cp unsquashfs %{buildroot}/bin/
popd

%files
/bin/mksquashfs
/bin/unsquashfs

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.4
- Initial RPM

