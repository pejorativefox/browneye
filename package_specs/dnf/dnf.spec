Name:       dnf
Version:    4.16.2
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
        -DLIBRARY_OUTPUT_PATH=%{_libdir} \
	..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
ln -sr %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/dnf
popd
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/bin/dnf
/usr/bin/dnf-3
/usr/bin/dnf-automatic-3
/etc/dnf/aliases.d/zypper.conf
/etc/dnf/automatic.conf
/etc/dnf/dnf.conf
/etc/dnf/protected.d/dnf.conf
/etc/dnf/protected.d/yum.conf
/etc/bash_completion.d/dnf
/etc/libreport/events.d/collect_dnf.conf
/etc/dnf/dnf-strict.conf
/etc/dnf/protected.d/python3-dnf.conf
/etc/logrotate.d/dnf
/usr/lib64/tmpfiles.d/dnf.conf
/usr/lib64/systemd/
/usr/lib64/python3.11/site-packages/dnf
/usr/share/locale/

%changelog
* Wed May 13 2020 Chris Statzer <chris.statzer@qq.com> 4.2.21
- Version upgrade to attempt to fix the bash completion issues.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.2.6
- Initial RPM

