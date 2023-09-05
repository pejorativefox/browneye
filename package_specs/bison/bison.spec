Name:       bison
Version:    3.8.2
Release:    1
Summary:    GNU parser generator
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
GNU parser generator

%prep
%setup -q

%build
%configure --docdir=/usr/share/doc/bison-%{version}
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*


%files
/usr/bin/bison
/usr/bin/yacc
/usr/lib64/liby.a
/usr/share/aclocal/bison-i18n.m4
/usr/share/bison/m4sugar/foreach.m4
/usr/share/bison/m4sugar/m4sugar.m4
/usr/share/bison/skeletons/bison.m4
/usr/share/bison/skeletons/c++-skel.m4
/usr/share/bison/skeletons/c++.m4
/usr/share/bison/skeletons/c-like.m4
/usr/share/bison/skeletons/c-skel.m4
/usr/share/bison/skeletons/c.m4
/usr/share/bison/skeletons/d-skel.m4
/usr/share/bison/skeletons/d.m4
/usr/share/bison/skeletons/glr.c
/usr/share/bison/skeletons/glr.cc
/usr/share/bison/skeletons/java-skel.m4
/usr/share/bison/skeletons/java.m4
/usr/share/bison/skeletons/lalr1.cc
/usr/share/bison/skeletons/lalr1.d
/usr/share/bison/skeletons/lalr1.java
/usr/share/bison/skeletons/location.cc
/usr/share/bison/skeletons/stack.hh
/usr/share/bison/skeletons/variant.hh
/usr/share/bison/skeletons/yacc.c
/usr/share/bison/README.md
/usr/share/bison/bison-default.css
/usr/share/bison/skeletons/glr2.cc
/usr/share/bison/skeletons/traceon.m4
/usr/share/bison/xslt/bison.xsl
/usr/share/bison/xslt/xml2dot.xsl
/usr/share/bison/xslt/xml2text.xsl
/usr/share/bison/xslt/xml2xhtml.xsl
/usr/share/info/bison.info.gz
/usr/share/locale/
/usr/share/man/man1/bison.1.gz
/usr/share/man/man1/yacc.1.gz
/usr/share/doc/bison-%{version}/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 3.8.2-1
- Version bump
