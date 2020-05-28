Name:       libsolv
Version:    0.7.10
Release:    2
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
      -DENABLE_PYTHON=ON ..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/bin/dumpsolv
/usr/bin/installcheck
/usr/bin/mergesolv
/usr/bin/repo2solv
/usr/bin/testsolv
/usr/include/solv/bitmap.h
/usr/include/solv/chksum.h
/usr/include/solv/dataiterator.h
/usr/include/solv/dirpool.h
/usr/include/solv/evr.h
/usr/include/solv/hash.h
/usr/include/solv/knownid.h
/usr/include/solv/policy.h
/usr/include/solv/pool.h
/usr/include/solv/poolarch.h
/usr/include/solv/poolid.h
/usr/include/solv/pooltypes.h
/usr/include/solv/poolvendor.h
/usr/include/solv/problems.h
/usr/include/solv/queue.h
/usr/include/solv/repo.h
/usr/include/solv/repo_solv.h
/usr/include/solv/repo_write.h
/usr/include/solv/repodata.h
/usr/include/solv/rules.h
/usr/include/solv/selection.h
/usr/include/solv/solv_xfopen.h
/usr/include/solv/solvable.h
/usr/include/solv/solver.h
/usr/include/solv/solverdebug.h
/usr/include/solv/solvversion.h
/usr/include/solv/strpool.h
/usr/include/solv/testcase.h
/usr/include/solv/tools_util.h
/usr/include/solv/transaction.h
/usr/include/solv/util.h
/usr/lib64/libsolv.so
/usr/lib64/libsolv.so.1
/usr/lib64/libsolvext.so
/usr/lib64/libsolvext.so.1
/usr/lib64/pkgconfig/libsolv.pc
/usr/lib64/pkgconfig/libsolvext.pc
/usr/share/cmake/Modules/FindLibSolv.cmake
/usr/share/man/man1/dumpsolv.1.gz
/usr/share/man/man1/installcheck.1.gz
/usr/share/man/man1/mergesolv.1.gz
/usr/share/man/man1/repo2solv.1.gz
/usr/share/man/man1/solv.1.gz
/usr/share/man/man1/testsolv.1.gz
/usr/share/man/man3/libsolv-bindings.3.gz
/usr/share/man/man3/libsolv-constantids.3.gz
/usr/share/man/man3/libsolv-history.3.gz
/usr/share/man/man3/libsolv-pool.3.gz
/usr/share/man/man3/libsolv.3.gz
/usr/bin/deltainfoxml2solv
/usr/bin/repomdxml2solv
/usr/bin/rpmdb2solv
/usr/bin/rpmmd2solv
/usr/bin/rpms2solv
/usr/bin/updateinfoxml2solv
/usr/include/solv/pool_fileconflicts.h
/usr/include/solv/pool_parserpmrichdep.h
/usr/include/solv/repo_deltainfoxml.h
/usr/include/solv/repo_repomdxml.h
/usr/include/solv/repo_rpmdb.h
/usr/include/solv/repo_rpmmd.h
/usr/include/solv/repo_updateinfoxml.h
/usr/share/man/man1/deltainfoxml2solv.1.gz
/usr/share/man/man1/repomdxml2solv.1.gz
/usr/share/man/man1/rpmdb2solv.1.gz
/usr/share/man/man1/rpmmd2solv.1.gz
/usr/share/man/man1/rpms2solv.1.gz
/usr/share/man/man1/updateinfoxml2solv.1.gz
/usr/lib/python3.7/site-packages/_solv.so
/usr/lib/python3.7/site-packages/solv.py

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.7.10
- Initial RPM

