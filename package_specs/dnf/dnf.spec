Name:       dnf
Version:    4.2.21
Release:    1
Summary:    Software management utility. 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

Requires: libdnf >= 0.39.1-1, rpm >= 4.14.2.1-1, python3-libcomps >= 0.1.14-1


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
ln -sr %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/dnf
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
/usr/lib/python3.7/site-packages/dnf/*
/usr/lib/systemd/*
/usr/share/locale/*
/etc/dnf/dnf-strict.conf
/usr/bin/dnf
/usr/share/bash-completion/completions/dnf

%changelog
* Wed May 13 2020 Chris Statzer <chris.statzer@qq.com> 4.2.21
- Version upgrade to attempt to fix the bash completion issues.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.2.6
- Initial RPM

