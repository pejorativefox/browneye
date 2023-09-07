Name:       libsolv
Version:    0.7.24
Release:    3
Summary:    Library for solving packages and reading repositories
License:    BSD
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Library for solving packages and reading repositories

%prep
%setup

%build
mkdir build
pushd build
cmake -DENABLE_COMPLEX_DEPS=1 -DENABLE_RPMDB=1 -DENABLE_RPMMD=1 \
      -DENABLE_RPMPKG=1 -DCMAKE_INSTALL_PREFIX:PATH=/usr \
      -DENABLE_PYTHON=ON \
      -DPYTHON_LIBRARY=/usr/lib64/libpython3.so \
      -DPYTHON_INCLUDE_DIR=/usr/include/python3.11/ \
       ..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
mkdir -pv %{buildroot}/usr/share/cmake-3.17/Modules/
mv %{buildroot}/usr/share/cmake/Modules/* %{buildroot}/usr/share/cmake-3.17/Modules/
popd

%files
/usr/bin/deltainfoxml2solv
/usr/bin/dumpsolv
/usr/bin/installcheck
/usr/bin/mergesolv
/usr/bin/repo2solv
/usr/bin/repomdxml2solv
/usr/bin/rpmdb2solv
/usr/bin/rpmmd2solv
/usr/bin/rpms2solv
/usr/bin/testsolv
/usr/bin/updateinfoxml2solv
/usr/lib64/libsolv.so
/usr/lib64/libsolv.so.1
/usr/lib64/libsolvext.so
/usr/lib64/libsolvext.so.1
/usr/lib64/pkgconfig/libsolv.pc
/usr/lib64/pkgconfig/libsolvext.pc
/usr/lib64/python3.11/site-packages/_solv.so
/usr/lib64/python3.11/site-packages/solv.py
/usr/include/solv
/usr/share/cmake-3.17/Modules/FindLibSolv.cmake
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.7.24
- Version bump

* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 0.7.10-3
- Terrible kludge to fix cmake module path. This needs to be fixed in a larger change.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.7.10
- Initial RPM

