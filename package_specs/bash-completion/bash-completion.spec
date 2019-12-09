Name:       bash-completion
Version:    2.10
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
TODO

%prep
%setup -a 0

%build
%configure 
%make_build

%install
%make_install

%files
/usr/share/bash-completion/*
/usr/etc/profile.d/bash_completion.sh
/usr/share/cmake/bash-completion/bash-completion-config-version.cmake
/usr/share/cmake/bash-completion/bash-completion-config.cmake
/usr/share/pkgconfig/bash-completion.pc

%changelog
# let's skip this for now
