Name:       dnf
Version:    4.2.6
Release:    1
Summary:    Software management utility. 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Software management utility. 

%prep
%setup

%build
mkdir build
pushd build
cmake 	-DPYTHON_DESIRED=3 \
	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
	-DWITH_MAN=0 \
	..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/etc/dnf/aliases.d/zypper.conf
/etc/dnf/automatic.conf
/etc/dnf/dnf.conf
/etc/dnf/protected.d/dnf.conf
/etc/dnf/protected.d/yum.conf
/etc/libreport/events.d/collect_dnf.conf
/etc/logrotate.d/dnf
/usr/bin/dnf-3
/usr/bin/dnf-automatic-3
/usr/lib/tmpfiles.d/dnf.conf
/usr/share/bash-completion/completions/dnf
/usr/lib/python3.7/site-packages/dnf/*
/usr/lib/systemd/*
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.2.6
- Initial RPM

