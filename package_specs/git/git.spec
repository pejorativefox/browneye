%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:       git
Version:    2.22.0
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

AutoReq: no

Requires: libc.so.6()(64bit), libcrypto.so.1.1()(64bit), libcurl.so.4()(64bit), libexpat.so.1()(64bit), libpthread.so.0()(64bit), librt.so.1()(64bit), libssl.so.1.1()(64bit), libz.so.1()(64bit), perl >= 0:5.004


%description
TODO

%prep
%setup -q -a0

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/etc/bash_completion.d/
cp contrib/completion/git-completion.bash %{buildroot}/etc/bash_completion.d/
%make_install

%files
/usr/bin/git
/usr/bin/git-cvsserver
/usr/bin/git-receive-pack
/usr/bin/git-shell
/usr/bin/git-upload-archive
/usr/bin/git-upload-pack
/usr/bin/gitk
/usr/libexec/git-core/*
/usr/share/locale/*
/usr/share/perl5/*
/usr/share/git-gui/
/usr/share/gitk/*
/usr/share/gitweb/*
/usr/share/git-core/*
/etc/bash_completion.d/git-completion.bash

%changelog
# let's skip this for now
