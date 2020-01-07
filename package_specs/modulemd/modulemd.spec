Name:       modulemd
Version:    1.8.16
Release:    1
Summary:    C Library for manipulating module metadata files 
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
C Library for manipulating module metadata files 

%prep
%setup

%build
mkdir build
pushd build
meson    --prefix=/usr \
         -Dwith_docs=false \
         -Dskip_clang_tidy=true \
         -Dskip_formatters=true \
         -Dskip_introspection=true \
         -Ddeveloper_build=false ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/modulemd-validator-v1
/usr/include/modulemd/modulemd-buildopts.h
/usr/include/modulemd/modulemd-component-module.h
/usr/include/modulemd/modulemd-component-rpm.h
/usr/include/modulemd/modulemd-component.h
/usr/include/modulemd/modulemd-defaults.h
/usr/include/modulemd/modulemd-dependencies.h
/usr/include/modulemd/modulemd-deprecated.h
/usr/include/modulemd/modulemd-improvedmodule.h
/usr/include/modulemd/modulemd-intent.h
/usr/include/modulemd/modulemd-module.h
/usr/include/modulemd/modulemd-modulestream.h
/usr/include/modulemd/modulemd-prioritizer.h
/usr/include/modulemd/modulemd-profile.h
/usr/include/modulemd/modulemd-servicelevel.h
/usr/include/modulemd/modulemd-simpleset.h
/usr/include/modulemd/modulemd-subdocument.h
/usr/include/modulemd/modulemd-translation-entry.h
/usr/include/modulemd/modulemd-translation.h
/usr/include/modulemd/modulemd.h
/usr/lib/libmodulemd.so
/usr/lib/libmodulemd.so.1
/usr/lib/libmodulemd.so.1.8.16
/usr/lib/pkgconfig/modulemd.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.8.16
- Initial RPM

