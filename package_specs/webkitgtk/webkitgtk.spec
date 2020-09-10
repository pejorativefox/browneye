Name:       webkitgtk
Version:    2.29.91
Release:    1
Summary:    WebKit is a cross-platform web browser engine.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
WebKit is a cross-platform web browser engine.

%prep
%setup

%build
mkdir build
pushd build
cmake .. -DPORT=GTK -DUSE_LIBHYPHEN=0 -DUSE_SYSTEMD=0 
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files

%changelog
* Thu Sep 10 2020 Chris Statzer <chris.statzer@qq.com> 2.29.91
- Initial RPM

