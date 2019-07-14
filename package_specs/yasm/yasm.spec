Name:       yasm
Version:    1.3.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
sed -i 's#) ytasm.*#)#' Makefile.in &&
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/yasm
/usr/include/libyasm-stdint.h
/usr/include/libyasm.h
/usr/include/libyasm/arch.h
/usr/include/libyasm/assocdat.h
/usr/include/libyasm/bitvect.h
/usr/include/libyasm/bytecode.h
/usr/include/libyasm/compat-queue.h
/usr/include/libyasm/coretype.h
/usr/include/libyasm/dbgfmt.h
/usr/include/libyasm/errwarn.h
/usr/include/libyasm/expr.h
/usr/include/libyasm/file.h
/usr/include/libyasm/floatnum.h
/usr/include/libyasm/hamt.h
/usr/include/libyasm/insn.h
/usr/include/libyasm/intnum.h
/usr/include/libyasm/inttree.h
/usr/include/libyasm/linemap.h
/usr/include/libyasm/listfmt.h
/usr/include/libyasm/md5.h
/usr/include/libyasm/module.h
/usr/include/libyasm/objfmt.h
/usr/include/libyasm/parser.h
/usr/include/libyasm/phash.h
/usr/include/libyasm/preproc.h
/usr/include/libyasm/section.h
/usr/include/libyasm/symrec.h
/usr/include/libyasm/valparam.h
/usr/include/libyasm/value.h
/usr/lib64/libyasm.a
/usr/share/man/man1/yasm.1.gz
/usr/share/man/man7/yasm_arch.7.gz
/usr/share/man/man7/yasm_dbgfmts.7.gz
/usr/share/man/man7/yasm_objfmts.7.gz
/usr/share/man/man7/yasm_parsers.7.gz

%changelog
# let's skip this for now

