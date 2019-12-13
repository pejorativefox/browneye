Name:       librepo
Version:    1.11.0
Release:    1
Summary:    A library providing C and Python (libcURL like) API for downloading packages.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
A library providing C and Python (libcURL like) API for downloading packages.

%prep
%setup

%build
mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DENABLE_DOCS=0 ..
%make_build 
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/include/librepo/checksum.h
/usr/include/librepo/downloader.h
/usr/include/librepo/downloader_internal.h
/usr/include/librepo/downloadtarget.h
/usr/include/librepo/fastestmirror.h
/usr/include/librepo/gpg.h
/usr/include/librepo/handle.h
/usr/include/librepo/librepo.h
/usr/include/librepo/metadata_downloader.h
/usr/include/librepo/metalink.h
/usr/include/librepo/mirrorlist.h
/usr/include/librepo/package_downloader.h
/usr/include/librepo/rcodes.h
/usr/include/librepo/repoconf.h
/usr/include/librepo/repomd.h
/usr/include/librepo/repoutil_yum.h
/usr/include/librepo/result.h
/usr/include/librepo/types.h
/usr/include/librepo/url_substitution.h
/usr/include/librepo/util.h
/usr/include/librepo/version.h
/usr/include/librepo/xmlparser.h
/usr/include/librepo/yum.h
/usr/lib/python2.7/site-packages/librepo/__init__.py
/usr/lib/python2.7/site-packages/librepo/_librepomodule.so
/usr/lib64/librepo.so
/usr/lib64/librepo.so.0
/usr/lib64/pkgconfig/librepo.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11.0
- Initial RPM

