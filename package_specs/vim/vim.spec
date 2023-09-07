Name:       vim
Version:    9.0.1677 
Release:    1
Summary:    vi Improved Text editor
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Vim is a highly configurable text editor built to make creating and changing any kind of text very efficient. It is included as "vi" with most UNIX systems and with Apple OS X. 

%prep
%setup -q

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
rm -rf %{buildroot}/usr/share/vim/vim90/tools/vim132

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
/usr/share/vim/
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 9.0.1677-1
- Version bump

* Fri May 15 2020 Chris Statzer <chris.statzer@qq.com> 8.1-4
- Removed gtk/X11 build

