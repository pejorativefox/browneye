Name:       python
Version:    3.7.2
Release:    3
Summary:    TODO
License:    GPL3
Source0:    Python-%{version}.tar.xz
Prefix:     /usr

BuildRequires: sqlite3
BuildRequires: bzip2
BuildRequires: openssl
BuildRequires: gnupg

Provides: /bin/python3

AutoReq: no
Requires: libbz2.so.1.0()(64bit), libc.so.6()(64bit), libcrypt.so.1()(64bit), libdl.so.2()(64bit), libexpat.so.1()(64bit) libffi.so.6()(64bit) libgdbm.so.6()(64bit) libgdbm_compat.so.4()(64bit) liblzma.so.5()(64bit) liblzma.so.5(XZ_5.0)(64bit) libm.so.6()(64bit), libncursesw.so.6()(64bit) libpanelw.so.6()(64bit) libpthread.so.0()(64bit), libreadline.so.8()(64bit) libsqlite3.so.0()(64bit) libssl.so.1.1()(64bit), libutil.so.1()(64bit), libuuid.so.1()(64bit), libz.so.1()(64bit)

%description
TODO

%prep
%setup -n Python-%{version}

%build
%configure --enable-shared     \
           --with-system-expat \
           --with-system-ffi   \
           --without-ensurepip
%make_build

%install
rm -rf %{buildroot}
%make_install
chmod -v 755 %{buildroot}/usr/lib64/libpython3.7m.so
chmod -v 755 %{buildroot}/usr/lib64/libpython3.so
rm -vf %{buildroot}%{_infodir}/dir*
rm -vrf %{buildroot}/usr/lib/python3.7/site-packages/pip/_internal/models/__pycache__
rm -rf %{buildroot}/usr/lib/python3.7/test
ln -s python3.7 %{buildroot}/usr/bin/python

%files
/usr/bin/2to3
/usr/bin/2to3-3.7
/usr/bin/idle3
/usr/bin/idle3.7
/usr/bin/pydoc3
/usr/bin/pydoc3.7
/usr/bin/python
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.7
/usr/bin/python3.7-config
/usr/bin/python3.7m
/usr/bin/python3.7m-config
/usr/bin/pyvenv
/usr/bin/pyvenv-3.7
/usr/include/python3.7m/
/usr/lib/python3.7/
/usr/lib64/libpython3.7m.so
/usr/lib64/libpython3.7m.so.1.0
/usr/lib64/libpython3.so
/usr/lib64/pkgconfig/python-3.7.pc
/usr/lib64/pkgconfig/python-3.7m.pc
/usr/lib64/pkgconfig/python3.pc
/usr/lib64/python3.7/
/usr/share/man/man1/python3.1.gz
/usr/share/man/man1/python3.7.1.gz

%changelog
* Tue May 19 2020 Chris Statzer <chris.statzer@qq.com> 3.7.2-2
- Removed left over tests folder.
