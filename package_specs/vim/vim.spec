Name:       vim
Version:    8.1
Release:    4
Summary:    vi Improved Text editor
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

AutoReq: no

Requires: libICE.so.6()(64bit), libSM.so.6()(64bit), libX11.so.6()(64bit), libXt.so.6()(64bit), libacl.so.1()(64bit), libc.so.6()(64bit), libdl.so.2()(64bit), libgdk-x11-2.0.so.0()(64bit), libgdk_pixbuf-2.0.so.0()(64bit), libgio-2.0.so.0()(64bit), libglib-2.0.so.0()(64bit), libgobject-2.0.so.0()(64bit), libgtk-x11-2.0.so.0()(64bit), libm.so.6()(64bit), libncursesw.so.6()(64bit), libpango-1.0.so.0()(64bit)

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

%files
/usr/bin/ex
/usr/bin/rview
/usr/bin/rvim
/usr/bin/view
/usr/bin/vim
/usr/bin/vimdiff
/usr/bin/vimtutor
/usr/bin/xxd
/usr/share/applications/gvim.desktop
/usr/share/applications/vim.desktop
/usr/share/icons/*
/usr/share/vim/*
/usr/share/man/*

%changelog
* Thu May 15 2020 Chris Statzer <chris.statzer@qq.com> 8.1-4
- Removed gtk/X11 build

