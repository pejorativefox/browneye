Name:       lua
Version:    5.4.6
Release:    2
Summary:    Lua High-level programming language
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

Provides: liblua.so.5.4()(64bit)

%description
Lua is a lightweight, high-level, multi-paradigm programming language designed primarily for embedded use in applications.

%prep
%setup -q

%build
cat > lua.pc << "EOF"
V=5.4
R=5.4.6

prefix=/usr
INSTALL_BIN=${prefix}/bin
INSTALL_INC=${prefix}/include
INSTALL_LIB=${prefix}/lib
INSTALL_MAN=${prefix}/share/man/man1
INSTALL_LMOD=${prefix}/share/lua/${V}
INSTALL_CMOD=${prefix}/lib/lua/${V}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: Lua
Description: An Extensible Extension Language
Version: ${R}
Requires:
Libs: -L${libdir} -llua -lm -ldl
Cflags: -I${includedir}
EOF

patch -Np1 -i ../../SOURCES/lua-5.4.6-shared_library-1.patch 
make linux

%install    
rm -rf %{buildroot}
pushd src
mkdir -pv %{buildroot}/usr/bin
mkdir -pv %{buildroot}/usr/include
mkdir -pv %{buildroot}/usr/lib64
chmod +x lua luac
install -v -m755 -D lua luac %{buildroot}/usr/bin
install -v -m644 -D lua.h luaconf.h lualib.h lauxlib.h lua.hpp %{buildroot}/usr/include
install -v -m644 -D liblua.so liblua.so.5.4 liblua.so.5.4.6 %{buildroot}/usr/lib64
popd
mkdir -pv %{buildroot}/usr/lib/pkgconfig/
install -v -m644 -D lua.pc %{buildroot}/usr/lib64/pkgconfig/lua.pc
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/lua
/usr/bin/luac
/usr/include/lauxlib.h
/usr/include/lua.h
/usr/include/lua.hpp
/usr/include/luaconf.h
/usr/include/lualib.h
/usr/lib64/liblua.so.5.4
/usr/lib64/liblua.so.5.4.6
/usr/lib64/liblua.so
/usr/lib64/pkgconfig/lua.pc

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 5.3.5-2
- Fixed executable bit on the main lua exe
