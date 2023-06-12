Name:       bubblewrap
Version:    0.4.0
Release:    1
Summary:    Unprivileged sandboxing tool 
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Unprivileged sandboxing tool 

%prep
%setup

%build
%configure --disable-man --with-priv-mode=setuid
%make_build

%install
rm -rf %{buildroot}
#%make_install
mkdir -p %{buildroot}/usr/bin
install -m 0755 bwrap  %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/share/bash-completion/completions
install -p completions/bash/bwrap %{buildroot}/usr/share/bash-completion/completions/bwrap
%files
/usr/bin/bwrap
/usr/share/bash-completion/completions/bwrap

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.4.0
- Initial RPM

