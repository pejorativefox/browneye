Name:       vim
Version:    8.1
Release:    5
Summary:    vi Improved Text editor
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Vim is a highly configurable text editor built to make creating and changing any kind of text very efficient. It is included as "vi" with most UNIX systems and with Apple OS X. 

%prep
%setup -n vim81

%build
echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h
%configure --enable-gui=no --without-x
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
rm %{buildroot}/usr/share/applications/gvim.desktop
rm -rf %{buildroot}/usr/share/icons/*
rm %{buildroot}/usr/share/vim/vim81/tools/vim132


%files
/usr/bin/ex
/usr/bin/rview
/usr/bin/rvim
/usr/bin/view
/usr/bin/vim
/usr/bin/vimdiff
/usr/bin/vimtutor
/usr/bin/xxd
/usr/share/applications/vim.desktop
/usr/share/vim/*
/usr/share/man/*

%changelog
* Thu May 15 2020 Chris Statzer <chris.statzer@qq.com> 8.1-4
- Removed gtk/X11 build

