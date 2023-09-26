Name:       polybar
Version:    3.6.3
Release:    1
Summary:    A fast and easy-to-use status bar
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

BuildRequires: xcb-util-wm

%description
A fast and easy-to-use status bar

%prep
%setup -n polybar-%{version}

%build
mkdir build
pushd build
cmake -DBUILD_DOC=0 -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/bin/polybar
/usr/bin/polybar-msg
/etc/polybar/config.ini
/usr/share/bash-completion/completions/polybar
/usr/share/zsh/site-functions/_polybar
/usr/share/zsh/site-functions/_polybar_msg

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.6.3-1
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.4.1
- Initial RPM

