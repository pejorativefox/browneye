Name:       readline
Version:    8.0
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --with-curses --disable-install-examples
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/readline/chardefs.h
/usr/include/readline/history.h
/usr/include/readline/keymaps.h
/usr/include/readline/readline.h
/usr/include/readline/rlconf.h
/usr/include/readline/rlstdc.h
/usr/include/readline/rltypedefs.h
/usr/include/readline/tilde.h
/usr/lib64/libhistory.a
/usr/lib64/libhistory.so
/usr/lib64/libhistory.so.8
/usr/lib64/libhistory.so.8.0
/usr/lib64/libreadline.a
/usr/lib64/libreadline.so
/usr/lib64/libreadline.so.8
/usr/lib64/libreadline.so.8.0
/usr/lib64/pkgconfig/readline.pc
/usr/share/doc/readline/CHANGES
/usr/share/doc/readline/INSTALL
/usr/share/doc/readline/README
/usr/share/info/history.info.gz
/usr/share/info/readline.info.gz
/usr/share/info/rluserman.info.gz
/usr/share/man/man3/history.3.gz
/usr/share/man/man3/readline.3.gz

%changelog
# let's skip this for now
