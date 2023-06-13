Name:       dosfstools
Version:    4.2
Release:    1
Summary:    dosfstools consists of the programs needed to create, check and label file systems of the FAT family. 
License:    GPL-3.0
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
dosfstools consists of the programs mkfs.fat, fsck.fat and fatlabel to create, check and label file systems of the FAT family. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/sbin/fatlabel
/usr/sbin/fsck.fat
/usr/sbin/mkfs.fat
/usr/share/doc/dosfstools/
/usr/share/man/man8/fatlabel.8.gz
/usr/share/man/man8/fsck.fat.8.gz
/usr/share/man/man8/mkfs.fat.8.gz

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

