Name:       zchunk
Version:    1.1.4
Release:    1
Summary:    A file format designed for highly efficient deltas while maintaining good compression 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
A file format designed for highly efficient deltas while maintaining good compression 

%prep
%setup

%build
mkdir build
pushd build
meson    --prefix=/usr
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/unzck
/usr/bin/zck
/usr/bin/zck_delta_size
/usr/bin/zck_gen_zdict
/usr/bin/zck_read_header
/usr/bin/zckdl
/usr/include/zck.h
/usr/lib64/libzck.so
/usr/lib64/libzck.so.1
/usr/lib64/libzck.so.1.1.4
/usr/lib64/pkgconfig/zck.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.1.4
- Initial RPM

