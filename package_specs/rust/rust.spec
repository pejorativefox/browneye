Name:       rust
Version:    1.31.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    rustc-1.31.1-x86_64-unknown-linux-gnu.tar.gz
Source1:    rust-std-1.31.1-x86_64-unknown-linux-gnu.tar.gz
Source2:    cargo-0.32.0-x86_64-unknown-linux-gnu.tar.gz

%description
TODO

%prep
rm -rf rust-1.31.1
mkdir rust-1.31.1
pushd rust-1.31.1
tar xf %{SOURCE0}
tar xf %{SOURCE1}
tar xf %{SOURCE2}
popd

%build

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/opt/rust
pushd rust-1.31.1
cp -r cargo-0.32.0-x86_64-unknown-linux-gnu/cargo/* %{buildroot}/opt/rust
cp -r rust-std-1.31.1-x86_64-unknown-linux-gnu/rust-std-x86_64-unknown-linux-gnu/* %{buildroot}/opt/rust
cp -r rustc-1.31.1-x86_64-unknown-linux-gnu/rustc/* %{buildroot}/opt/rust
popd


%files
/opt/rust/bin/cargo
/opt/rust/bin/rust-gdb
/opt/rust/bin/rust-lldb
/opt/rust/bin/rustc
/opt/rust/bin/rustdoc
/opt/rust/etc/bash_completion.d/cargo
/opt/rust/lib/libarena-187156a709fcf0c7.so
/opt/rust/lib/libfmt_macros-ca7c986c9411706e.so
/opt/rust/lib/libgraphviz-79de91bf8ef1dffb.so
/opt/rust/lib/libproc_macro-eb9b1f5dc4b73ebd.so
/opt/rust/lib/librustc-c0b0e3599e0c7f59.so
/opt/rust/lib/librustc_allocator-a868ba4fcd22648f.so
/opt/rust/lib/librustc_borrowck-c4ab9d6bcdc70190.so
/opt/rust/lib/librustc_codegen_utils-c0aa64ad3e265a1a.so
/opt/rust/lib/librustc_cratesio_shim-edaa44f354d2dc64.so
/opt/rust/lib/librustc_data_structures-e097383a5270f2c8.so
/opt/rust/lib/librustc_driver-3f6fac6fa480c6f4.so
/opt/rust/lib/librustc_errors-1e5cc81238ac8ca0.so
/opt/rust/lib/librustc_fs_util-77858047dfa08d44.so
/opt/rust/lib/librustc_incremental-cf01ba19661e7def.so
/opt/rust/lib/librustc_lint-29d30c40d3d31ed6.so
/opt/rust/lib/librustc_metadata-c75dc02cbecde802.so
/opt/rust/lib/librustc_metadata_utils-829423e66af86a97.so
/opt/rust/lib/librustc_mir-78500445c70e0286.so
/opt/rust/lib/librustc_passes-b6f36babf2fb0d4b.so
/opt/rust/lib/librustc_platform_intrinsics-dddaeac463f2f7e4.so
/opt/rust/lib/librustc_plugin-797e499c06011f36.so
/opt/rust/lib/librustc_privacy-82151cd0ca33d30c.so
/opt/rust/lib/librustc_resolve-8db376cd7233cf6f.so
/opt/rust/lib/librustc_save_analysis-b1418db30318b38b.so
/opt/rust/lib/librustc_target-3cd481a0a1bb4ab4.so
/opt/rust/lib/librustc_traits-be4342b0583bdf25.so
/opt/rust/lib/librustc_typeck-5c674a25a0103a36.so
/opt/rust/lib/libserialize-3deaf219532d0efb.so
/opt/rust/lib/libstd-89cf9eb8d404bb7b.so
/opt/rust/lib/libsyntax-8b4b84ccec0d2e12.so
/opt/rust/lib/libsyntax_ext-75f2a9756d859f4b.so
/opt/rust/lib/libsyntax_pos-31f39647344993a7.so
/opt/rust/lib/libterm-908202716e5d489b.so
/opt/rust/lib/libtest-69521d05599afa76.so
/opt/rust/lib/rustlib/etc/debugger_pretty_printers_common.py
/opt/rust/lib/rustlib/etc/gdb_load_rust_pretty_printers.py
/opt/rust/lib/rustlib/etc/gdb_rust_pretty_printing.py
/opt/rust/lib/rustlib/etc/lldb_rust_formatters.py
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/bin/rust-lld
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/codegen-backends/librustc_codegen_llvm-emscripten.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/codegen-backends/librustc_codegen_llvm-llvm.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libLLVM-8svn.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liballoc-ac8a19e2dea4f5a1.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liballoc_jemalloc-daf4b30ba0aa7eb6.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liballoc_system-34fc26c16207806e.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libarena-187156a709fcf0c7.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libarrayvec-7b71b8246354acdc.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libatty-7d7331f8048799b0.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libbacktrace-2668697d157ac255.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libbacktrace_sys-131662f3d32fdf9e.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libbitflags-ec4bc4f666d29534.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libbyteorder-101a2c206a1e5215.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcfg_if-aa852d9d89644df5.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libchalk_engine-384c44256cfd36c2.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libchalk_macros-a33243267fb5b805.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcompiler_builtins-5f64e7823d30511e.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcore-bc99d396b91fe14a.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcrossbeam_deque-cd07687919933af5.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcrossbeam_epoch-ee25b265d7372d7e.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcrossbeam_utils-301057c322bd1837.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libdatafrog-e3937c7e950e716c.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libeither-1e24a479a93a7ed9.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libena-c973c79f77bfc6fb.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libenv_logger-adc22bc91213d527.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libflate2-3d9a65fea9098596.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libfmt_macros-ca7c986c9411706e.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libgetopts-ff1e6faf188c3818.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libgraphviz-79de91bf8ef1dffb.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libhumantime-9598d3dffb611df2.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libjobserver-6bdd233f10b397e3.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblazy_static-4fc861bbd34bef95.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblazy_static-c7fed8884a11c4e7.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblibc-5d72f72e0dcb886e.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblibc-d0b3565c39ede68e.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblock_api-52a1ce3f9bccebcf.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblog-8dcca4b89208a39d.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblog_settings-3a4d3d4bbd4b4e16.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libmemoffset-4bdc4c2b3f6601d4.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libminiz_sys-a9fdb0b104a147ec.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libnodrop-6d106adb71331729.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libnum_cpus-ce4bdc19ecb09c72.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libowning_ref-1367646e44755cb1.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libpanic_abort-ce592ea191b58149.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libpanic_unwind-b4f2368c97086610.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libparking_lot-a56a9703650176ca.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libparking_lot_core-48292ff22ae5afa1.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libparking_lot_core-4c59e5fe1aa47e9a.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libpolonius_engine-812a86d50368ffb5.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libproc_macro-eb9b1f5dc4b73ebd.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libprofiler_builtins-6dee678996aec96f.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libquick_error-ef95b2893b1ae97d.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librand-4232681b135e338e.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librand-ef20ce96e9f8d24c.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librand_core-4c6bac8492ee9bc9.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libremove_dir_all-8f693c4a4a902a01.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librls_data-5a53a896343dc289.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librls_span-bb716f60ff7984d4.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc-c0b0e3599e0c7f59.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_allocator-a868ba4fcd22648f.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_apfloat-f8103049c8aaba96.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_asan-0b9cf611ddba8664.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_borrowck-c4ab9d6bcdc70190.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_codegen_utils-c0aa64ad3e265a1a.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_cratesio_shim-edaa44f354d2dc64.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_data_structures-e097383a5270f2c8.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_demangle-f9cc578b1da26523.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_driver-3f6fac6fa480c6f4.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_errors-1e5cc81238ac8ca0.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_fs_util-77858047dfa08d44.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_hash-b64ef6f7b20b1cb0.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_incremental-cf01ba19661e7def.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_lint-29d30c40d3d31ed6.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_lsan-62b164d3eee710b6.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_metadata-c75dc02cbecde802.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_metadata_utils-829423e66af86a97.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_mir-78500445c70e0286.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_msan-d8ef0f4eca3b333f.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_passes-b6f36babf2fb0d4b.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_platform_intrinsics-dddaeac463f2f7e4.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_plugin-797e499c06011f36.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_privacy-82151cd0ca33d30c.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_rayon-76ed0ffffe9cd595.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_rayon_core-4166b21f14ffab74.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_resolve-8db376cd7233cf6f.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_save_analysis-b1418db30318b38b.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_serialize-0a2b6421386f9857.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_target-3cd481a0a1bb4ab4.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_traits-be4342b0583bdf25.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_tsan-b27f68b01b841472.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_typeck-5c674a25a0103a36.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libscoped_tls-716f8aff3255cbec.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libscopeguard-5ebc186dde696ffb.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libserialize-3deaf219532d0efb.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libserialize-3deaf219532d0efb.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libsmallvec-066b69ea7dac6f2b.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstable_deref_trait-0c45ae930812287f.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd-89cf9eb8d404bb7b.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd-89cf9eb8d404bb7b.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libsyntax-8b4b84ccec0d2e12.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libsyntax_ext-75f2a9756d859f4b.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libsyntax_pos-31f39647344993a7.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libtempfile-40257977cfe16aa2.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libterm-908202716e5d489b.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libterm-908202716e5d489b.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libtermcolor-01d39f34a0a7c75f.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libtest-69521d05599afa76.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libtest-69521d05599afa76.so
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libunicode_width-8d352fbc93320466.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libunreachable-29ad726dbf0328e5.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libunwind-4c51ac82f70822c1.rlib
/opt/rust/lib/rustlib/x86_64-unknown-linux-gnu/lib/libvoid-aee951f204c421cf.rlib
/opt/rust/manifest.in
/opt/rust/share/doc/cargo/LICENSE-APACHE
/opt/rust/share/doc/cargo/LICENSE-MIT
/opt/rust/share/doc/cargo/LICENSE-THIRD-PARTY
/opt/rust/share/doc/cargo/README.md
/opt/rust/share/doc/rust/COPYRIGHT
/opt/rust/share/doc/rust/LICENSE-APACHE
/opt/rust/share/doc/rust/LICENSE-MIT
/opt/rust/share/doc/rust/README.md
/opt/rust/share/man/man1/cargo-bench.1
/opt/rust/share/man/man1/cargo-build.1
/opt/rust/share/man/man1/cargo-check.1
/opt/rust/share/man/man1/cargo-clean.1
/opt/rust/share/man/man1/cargo-doc.1
/opt/rust/share/man/man1/cargo-fetch.1
/opt/rust/share/man/man1/cargo-generate-lockfile.1
/opt/rust/share/man/man1/cargo-init.1
/opt/rust/share/man/man1/cargo-install.1
/opt/rust/share/man/man1/cargo-login.1
/opt/rust/share/man/man1/cargo-metadata.1
/opt/rust/share/man/man1/cargo-new.1
/opt/rust/share/man/man1/cargo-owner.1
/opt/rust/share/man/man1/cargo-package.1
/opt/rust/share/man/man1/cargo-pkgid.1
/opt/rust/share/man/man1/cargo-publish.1
/opt/rust/share/man/man1/cargo-run.1
/opt/rust/share/man/man1/cargo-rustc.1
/opt/rust/share/man/man1/cargo-rustdoc.1
/opt/rust/share/man/man1/cargo-search.1
/opt/rust/share/man/man1/cargo-test.1
/opt/rust/share/man/man1/cargo-uninstall.1
/opt/rust/share/man/man1/cargo-update.1
/opt/rust/share/man/man1/cargo-version.1
/opt/rust/share/man/man1/cargo-yank.1
/opt/rust/share/man/man1/cargo.1
/opt/rust/share/man/man1/rustc.1
/opt/rust/share/man/man1/rustdoc.1
/opt/rust/share/zsh/site-functions/_cargo

%changelog
# let's skip this for now

