Name:       polybar
Version:    3.4.1
Release:    1
Summary:    A fast and easy-to-use status bar
License:    GPL
Source0:    %{name}-%{version}.tar
Prefix:     /usr

%description
A fast and easy-to-use status bar

%prep
%setup -n polybar

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
/usr/share/bash-completion/completions/polybar
/usr/share/doc/polybar/config
/usr/share/zsh/site-functions/_polybar
/usr/share/zsh/site-functions/_polybar_msg

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.4.1
- Initial RPM

