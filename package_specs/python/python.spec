Name:       python
Version:    3.11.4
Release:    1
Summary:    The Python programming language
License:    GPL3
Source0:    Python-%{version}.tar.xz
Prefix:     /usr

#BuildRequires: sqlite3
#BuildRequires: bzip2
#BuildRequires: openssl
#BuildRequires: gnupg

Provides: /bin/python3, /bin/python

AutoReq: no
Requires: libbz2.so.1.0()(64bit), libc.so.6()(64bit), libcrypt.so.1()(64bit), libdl.so.2()(64bit), libexpat.so.1()(64bit) libffi.so.6()(64bit) libgdbm.so.6()(64bit) libgdbm_compat.so.4()(64bit) liblzma.so.5()(64bit) liblzma.so.5(XZ_5.0)(64bit) libm.so.6()(64bit), libncursesw.so.6()(64bit) libpanelw.so.6()(64bit) libpthread.so.0()(64bit), libreadline.so.8()(64bit) libsqlite3.so.0()(64bit) libssl.so.1.1()(64bit), libutil.so.1()(64bit), libuuid.so.1()(64bit), libz.so.1()(64bit)

%description
The Python programming language

%prep
%setup -q -n Python-%{version}

%build
%configure  --enable-shared        \
            --with-system-expat    \
            --with-system-ffi      \
            --enable-optimizations \
            --with-platlibdir=lib64
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
ln -s python3.11 %{buildroot}/usr/bin/python

%files -f ../../SOURCES/python.filelist

%changelog
* Tue May 19 2020 Chris Statzer <chris.statzer@qq.com> 3.7.2-2
- Removed left over tests folder.
