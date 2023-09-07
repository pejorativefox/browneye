Name:       pcre
Version:    8.42
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2


%description
TODO

%prep
%setup -a 0

%build
%configure  --docdir=/usr/share/doc/pcre-8.42 \
            --enable-unicode-properties       \
            --enable-pcre16                   \
            --enable-pcre32                   \
            --enable-pcregrep-libz            \
            --enable-pcregrep-libbz2          \
            --enable-pcretest-libreadline     \
            --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/pcre-config
/usr/bin/pcregrep
/usr/bin/pcretest
/usr/include/pcre.h
/usr/include/pcre_scanner.h
/usr/include/pcre_stringpiece.h
/usr/include/pcrecpp.h
/usr/include/pcrecpparg.h
/usr/include/pcreposix.h
/usr/lib64/libpcre.so
/usr/lib64/libpcre.so.1
/usr/lib64/libpcre.so.1.2.10
/usr/lib64/libpcre16.so
/usr/lib64/libpcre16.so.0
/usr/lib64/libpcre16.so.0.2.10
/usr/lib64/libpcre32.so
/usr/lib64/libpcre32.so.0
/usr/lib64/libpcre32.so.0.0.10
/usr/lib64/libpcrecpp.so
/usr/lib64/libpcrecpp.so.0
/usr/lib64/libpcrecpp.so.0.0.1
/usr/lib64/libpcreposix.so
/usr/lib64/libpcreposix.so.0
/usr/lib64/libpcreposix.so.0.0.6
/usr/lib64/pkgconfig/libpcre.pc
/usr/lib64/pkgconfig/libpcre16.pc
/usr/lib64/pkgconfig/libpcre32.pc
/usr/lib64/pkgconfig/libpcrecpp.pc
/usr/lib64/pkgconfig/libpcreposix.pc
/usr/share/doc/pcre-8.42/AUTHORS
/usr/share/doc/pcre-8.42/COPYING
/usr/share/doc/pcre-8.42/ChangeLog
/usr/share/doc/pcre-8.42/LICENCE
/usr/share/doc/pcre-8.42/NEWS
/usr/share/doc/pcre-8.42/README
/usr/share/doc/pcre-8.42/html/NON-AUTOTOOLS-BUILD.txt
/usr/share/doc/pcre-8.42/html/README.txt
/usr/share/doc/pcre-8.42/html/index.html
/usr/share/doc/pcre-8.42/html/pcre-config.html
/usr/share/doc/pcre-8.42/html/pcre.html
/usr/share/doc/pcre-8.42/html/pcre16.html
/usr/share/doc/pcre-8.42/html/pcre32.html
/usr/share/doc/pcre-8.42/html/pcre_assign_jit_stack.html
/usr/share/doc/pcre-8.42/html/pcre_compile.html
/usr/share/doc/pcre-8.42/html/pcre_compile2.html
/usr/share/doc/pcre-8.42/html/pcre_config.html
/usr/share/doc/pcre-8.42/html/pcre_copy_named_substring.html
/usr/share/doc/pcre-8.42/html/pcre_copy_substring.html
/usr/share/doc/pcre-8.42/html/pcre_dfa_exec.html
/usr/share/doc/pcre-8.42/html/pcre_exec.html
/usr/share/doc/pcre-8.42/html/pcre_free_study.html
/usr/share/doc/pcre-8.42/html/pcre_free_substring.html
/usr/share/doc/pcre-8.42/html/pcre_free_substring_list.html
/usr/share/doc/pcre-8.42/html/pcre_fullinfo.html
/usr/share/doc/pcre-8.42/html/pcre_get_named_substring.html
/usr/share/doc/pcre-8.42/html/pcre_get_stringnumber.html
/usr/share/doc/pcre-8.42/html/pcre_get_stringtable_entries.html
/usr/share/doc/pcre-8.42/html/pcre_get_substring.html
/usr/share/doc/pcre-8.42/html/pcre_get_substring_list.html
/usr/share/doc/pcre-8.42/html/pcre_jit_exec.html
/usr/share/doc/pcre-8.42/html/pcre_jit_stack_alloc.html
/usr/share/doc/pcre-8.42/html/pcre_jit_stack_free.html
/usr/share/doc/pcre-8.42/html/pcre_maketables.html
/usr/share/doc/pcre-8.42/html/pcre_pattern_to_host_byte_order.html
/usr/share/doc/pcre-8.42/html/pcre_refcount.html
/usr/share/doc/pcre-8.42/html/pcre_study.html
/usr/share/doc/pcre-8.42/html/pcre_utf16_to_host_byte_order.html
/usr/share/doc/pcre-8.42/html/pcre_utf32_to_host_byte_order.html
/usr/share/doc/pcre-8.42/html/pcre_version.html
/usr/share/doc/pcre-8.42/html/pcreapi.html
/usr/share/doc/pcre-8.42/html/pcrebuild.html
/usr/share/doc/pcre-8.42/html/pcrecallout.html
/usr/share/doc/pcre-8.42/html/pcrecompat.html
/usr/share/doc/pcre-8.42/html/pcrecpp.html
/usr/share/doc/pcre-8.42/html/pcredemo.html
/usr/share/doc/pcre-8.42/html/pcregrep.html
/usr/share/doc/pcre-8.42/html/pcrejit.html
/usr/share/doc/pcre-8.42/html/pcrelimits.html
/usr/share/doc/pcre-8.42/html/pcrematching.html
/usr/share/doc/pcre-8.42/html/pcrepartial.html
/usr/share/doc/pcre-8.42/html/pcrepattern.html
/usr/share/doc/pcre-8.42/html/pcreperform.html
/usr/share/doc/pcre-8.42/html/pcreposix.html
/usr/share/doc/pcre-8.42/html/pcreprecompile.html
/usr/share/doc/pcre-8.42/html/pcresample.html
/usr/share/doc/pcre-8.42/html/pcrestack.html
/usr/share/doc/pcre-8.42/html/pcresyntax.html
/usr/share/doc/pcre-8.42/html/pcretest.html
/usr/share/doc/pcre-8.42/html/pcreunicode.html
/usr/share/doc/pcre-8.42/pcre-config.txt
/usr/share/doc/pcre-8.42/pcre.txt
/usr/share/doc/pcre-8.42/pcregrep.txt
/usr/share/doc/pcre-8.42/pcretest.txt
/usr/share/man/man1/pcre-config.1.gz
/usr/share/man/man1/pcregrep.1.gz
/usr/share/man/man1/pcretest.1.gz
/usr/share/man/man3/pcre.3.gz
/usr/share/man/man3/pcre16.3.gz
/usr/share/man/man3/pcre16_assign_jit_stack.3.gz
/usr/share/man/man3/pcre16_compile.3.gz
/usr/share/man/man3/pcre16_compile2.3.gz
/usr/share/man/man3/pcre16_config.3.gz
/usr/share/man/man3/pcre16_copy_named_substring.3.gz
/usr/share/man/man3/pcre16_copy_substring.3.gz
/usr/share/man/man3/pcre16_dfa_exec.3.gz
/usr/share/man/man3/pcre16_exec.3.gz
/usr/share/man/man3/pcre16_free_study.3.gz
/usr/share/man/man3/pcre16_free_substring.3.gz
/usr/share/man/man3/pcre16_free_substring_list.3.gz
/usr/share/man/man3/pcre16_fullinfo.3.gz
/usr/share/man/man3/pcre16_get_named_substring.3.gz
/usr/share/man/man3/pcre16_get_stringnumber.3.gz
/usr/share/man/man3/pcre16_get_stringtable_entries.3.gz
/usr/share/man/man3/pcre16_get_substring.3.gz
/usr/share/man/man3/pcre16_get_substring_list.3.gz
/usr/share/man/man3/pcre16_jit_exec.3.gz
/usr/share/man/man3/pcre16_jit_stack_alloc.3.gz
/usr/share/man/man3/pcre16_jit_stack_free.3.gz
/usr/share/man/man3/pcre16_maketables.3.gz
/usr/share/man/man3/pcre16_pattern_to_host_byte_order.3.gz
/usr/share/man/man3/pcre16_refcount.3.gz
/usr/share/man/man3/pcre16_study.3.gz
/usr/share/man/man3/pcre16_utf16_to_host_byte_order.3.gz
/usr/share/man/man3/pcre16_version.3.gz
/usr/share/man/man3/pcre32.3.gz
/usr/share/man/man3/pcre32_assign_jit_stack.3.gz
/usr/share/man/man3/pcre32_compile.3.gz
/usr/share/man/man3/pcre32_compile2.3.gz
/usr/share/man/man3/pcre32_config.3.gz
/usr/share/man/man3/pcre32_copy_named_substring.3.gz
/usr/share/man/man3/pcre32_copy_substring.3.gz
/usr/share/man/man3/pcre32_dfa_exec.3.gz
/usr/share/man/man3/pcre32_exec.3.gz
/usr/share/man/man3/pcre32_free_study.3.gz
/usr/share/man/man3/pcre32_free_substring.3.gz
/usr/share/man/man3/pcre32_free_substring_list.3.gz
/usr/share/man/man3/pcre32_fullinfo.3.gz
/usr/share/man/man3/pcre32_get_named_substring.3.gz
/usr/share/man/man3/pcre32_get_stringnumber.3.gz
/usr/share/man/man3/pcre32_get_stringtable_entries.3.gz
/usr/share/man/man3/pcre32_get_substring.3.gz
/usr/share/man/man3/pcre32_get_substring_list.3.gz
/usr/share/man/man3/pcre32_jit_exec.3.gz
/usr/share/man/man3/pcre32_jit_stack_alloc.3.gz
/usr/share/man/man3/pcre32_jit_stack_free.3.gz
/usr/share/man/man3/pcre32_maketables.3.gz
/usr/share/man/man3/pcre32_pattern_to_host_byte_order.3.gz
/usr/share/man/man3/pcre32_refcount.3.gz
/usr/share/man/man3/pcre32_study.3.gz
/usr/share/man/man3/pcre32_utf32_to_host_byte_order.3.gz
/usr/share/man/man3/pcre32_version.3.gz
/usr/share/man/man3/pcre_assign_jit_stack.3.gz
/usr/share/man/man3/pcre_compile.3.gz
/usr/share/man/man3/pcre_compile2.3.gz
/usr/share/man/man3/pcre_config.3.gz
/usr/share/man/man3/pcre_copy_named_substring.3.gz
/usr/share/man/man3/pcre_copy_substring.3.gz
/usr/share/man/man3/pcre_dfa_exec.3.gz
/usr/share/man/man3/pcre_exec.3.gz
/usr/share/man/man3/pcre_free_study.3.gz
/usr/share/man/man3/pcre_free_substring.3.gz
/usr/share/man/man3/pcre_free_substring_list.3.gz
/usr/share/man/man3/pcre_fullinfo.3.gz
/usr/share/man/man3/pcre_get_named_substring.3.gz
/usr/share/man/man3/pcre_get_stringnumber.3.gz
/usr/share/man/man3/pcre_get_stringtable_entries.3.gz
/usr/share/man/man3/pcre_get_substring.3.gz
/usr/share/man/man3/pcre_get_substring_list.3.gz
/usr/share/man/man3/pcre_jit_exec.3.gz
/usr/share/man/man3/pcre_jit_stack_alloc.3.gz
/usr/share/man/man3/pcre_jit_stack_free.3.gz
/usr/share/man/man3/pcre_maketables.3.gz
/usr/share/man/man3/pcre_pattern_to_host_byte_order.3.gz
/usr/share/man/man3/pcre_refcount.3.gz
/usr/share/man/man3/pcre_study.3.gz
/usr/share/man/man3/pcre_utf16_to_host_byte_order.3.gz
/usr/share/man/man3/pcre_utf32_to_host_byte_order.3.gz
/usr/share/man/man3/pcre_version.3.gz
/usr/share/man/man3/pcreapi.3.gz
/usr/share/man/man3/pcrebuild.3.gz
/usr/share/man/man3/pcrecallout.3.gz
/usr/share/man/man3/pcrecompat.3.gz
/usr/share/man/man3/pcrecpp.3.gz
/usr/share/man/man3/pcredemo.3.gz
/usr/share/man/man3/pcrejit.3.gz
/usr/share/man/man3/pcrelimits.3.gz
/usr/share/man/man3/pcrematching.3.gz
/usr/share/man/man3/pcrepartial.3.gz
/usr/share/man/man3/pcrepattern.3.gz
/usr/share/man/man3/pcreperform.3.gz
/usr/share/man/man3/pcreposix.3.gz
/usr/share/man/man3/pcreprecompile.3.gz
/usr/share/man/man3/pcresample.3.gz
/usr/share/man/man3/pcrestack.3.gz
/usr/share/man/man3/pcresyntax.3.gz
/usr/share/man/man3/pcreunicode.3.gz

%changelog
# let's skip this for now

