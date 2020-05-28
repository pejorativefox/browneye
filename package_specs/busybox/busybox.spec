Name:       busybox
Version:    1.31.1
Release:    1
Summary:    BusyBox combines tiny versions of many common UNIX utilities into a single small executable.
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
BusyBox combines tiny versions of many common UNIX utilities into a single small executable.

%prep
%setup

%build
make defconfig
%make_build

%install
rm -rf %{buildroot}
%make_install
cp -r _install %{buildroot}

%files
/bin/*
/sbin/*
/usr/bin/*
/usr/sbin/*
/linuxrc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.31.1
- Initial RPM

