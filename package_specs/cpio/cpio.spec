Name:       cpio 
Version:    2.14
Release:    1
Summary:    GNU cpio copies files into or out of a cpio or tar archive. The archive can be another file on the disk, a magnetic tape, or a pipe. 
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
GNU cpio copies files into or out of a cpio or tar archive. The archive can be another file on the disk, a magnetic tape, or a pipe. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/libexec/rmt
rm -rf %{buildroot}/usr/share/info/dir
rm -rf %{buildroot}/usr/share/man/

%files
/usr/bin/cpio
/usr/share/info/cpio.info.gz
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM

