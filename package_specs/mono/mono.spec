Name:       mono
Version:    6.8.0.123
Release:    1
Summary:    Mono open source ECMA CLI, C# and .NET implementation.
License:    MIT
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Mono open source ECMA CLI, C# and .NET implementation.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/al
/usr/bin/al2
/usr/bin/aprofutil
/usr/bin/caspol
/usr/bin/cccheck
/usr/bin/ccrewrite
/usr/bin/cert-sync
/usr/bin/cert2spc
/usr/bin/certmgr
/usr/bin/chktrust
/usr/bin/crlupdate
/usr/bin/csc
/usr/bin/csharp
/usr/bin/csi
/usr/bin/disco
/usr/bin/dmcs
/usr/bin/dtd2rng
/usr/bin/dtd2xsd
/usr/bin/gacutil
/usr/bin/gacutil2
/usr/bin/genxs
/usr/bin/httpcfg
/usr/bin/ikdasm
/usr/bin/ilasm
/usr/bin/illinkanalyzer
/usr/bin/installvst
/usr/bin/lc
/usr/bin/macpack
/usr/bin/makecert
/usr/bin/mconfig
/usr/bin/mcs
/usr/bin/mdassembler
/usr/bin/mdbrebase
/usr/bin/mdoc
/usr/bin/mdoc-assemble
/usr/bin/mdoc-export-html
/usr/bin/mdoc-export-msxdoc
/usr/bin/mdoc-update
/usr/bin/mdoc-validate
/usr/bin/mdvalidater
/usr/bin/mkbundle
/usr/bin/mod
/usr/bin/mono
/usr/bin/mono-api-html
/usr/bin/mono-api-info
/usr/bin/mono-boehm
/usr/bin/mono-cil-strip
/usr/bin/mono-configuration-crypto
/usr/bin/mono-find-provides
/usr/bin/mono-find-requires
/usr/bin/mono-gdb.py
/usr/bin/mono-hang-watchdog
/usr/bin/mono-heapviz
/usr/bin/mono-package-runtime
/usr/bin/mono-service
/usr/bin/mono-service2
/usr/bin/mono-sgen
/usr/bin/mono-sgen-gdb.py
/usr/bin/mono-shlib-cop
/usr/bin/mono-symbolicate
/usr/bin/mono-test-install
/usr/bin/mono-xmltool
/usr/bin/monodis
/usr/bin/monodocer
/usr/bin/monodocs2html
/usr/bin/monodocs2slashdoc
/usr/bin/monolinker
/usr/bin/monop
/usr/bin/monop2
/usr/bin/mozroots
/usr/bin/mprof-report
/usr/bin/pdb2mdb
/usr/bin/pedump
/usr/bin/permview
/usr/bin/peverify
/usr/bin/resgen
/usr/bin/resgen2
/usr/bin/secutil
/usr/bin/setreg
/usr/bin/sgen
/usr/bin/sgen-grep-binprot
/usr/bin/signcode
/usr/bin/sn
/usr/bin/soapsuds
/usr/bin/sqlmetal
/usr/bin/sqlsharp
/usr/bin/svcutil
/usr/bin/vbc
/usr/bin/wsdl
/usr/bin/wsdl2
/usr/bin/xbuild
/usr/bin/xsd
/usr/etc/mono/
/usr/include/mono-2.0/
/usr/lib/mono-source-libs/
/usr/lib/mono/
/usr/lib/monodoc/
/usr/lib64/
/usr/lib64/mono/lldb/mono.py
/usr/lib64/pkgconfig/
/usr/share/libgc-mono/
/usr/share/locale/
/usr/share/mono-2.0/
/usr/share/man/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 6.8.0.123-1
- Initial RPM

