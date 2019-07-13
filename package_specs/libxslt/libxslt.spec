Name:       libxslt
Version:    1.1.33
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
sed -i s/3000/5000/ libxslt/transform.c doc/xsltproc.{1,xml} 
%configure  --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/xslt-config
/usr/bin/xsltproc
/usr/include/libexslt/exslt.h
/usr/include/libexslt/exsltconfig.h
/usr/include/libexslt/exsltexports.h
/usr/include/libxslt/attributes.h
/usr/include/libxslt/documents.h
/usr/include/libxslt/extensions.h
/usr/include/libxslt/extra.h
/usr/include/libxslt/functions.h
/usr/include/libxslt/imports.h
/usr/include/libxslt/keys.h
/usr/include/libxslt/namespaces.h
/usr/include/libxslt/numbersInternals.h
/usr/include/libxslt/pattern.h
/usr/include/libxslt/preproc.h
/usr/include/libxslt/security.h
/usr/include/libxslt/templates.h
/usr/include/libxslt/transform.h
/usr/include/libxslt/variables.h
/usr/include/libxslt/xslt.h
/usr/include/libxslt/xsltInternals.h
/usr/include/libxslt/xsltconfig.h
/usr/include/libxslt/xsltexports.h
/usr/include/libxslt/xsltlocale.h
/usr/include/libxslt/xsltutils.h
/usr/lib64/libexslt.la
/usr/lib64/libexslt.so
/usr/lib64/libexslt.so.0
/usr/lib64/libexslt.so.0.8.20
/usr/lib64/libxslt.la
/usr/lib64/libxslt.so
/usr/lib64/libxslt.so.1
/usr/lib64/libxslt.so.1.1.33
/usr/lib64/pkgconfig/libexslt.pc
/usr/lib64/pkgconfig/libxslt.pc
/usr/lib64/xsltConf.sh
/usr/share/aclocal/libxslt.m4
/usr/share/doc/libxslt-1.1.33/html/API.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk0.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk1.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk10.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk11.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk12.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk13.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk2.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk3.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk4.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk5.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk6.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk7.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk8.html
/usr/share/doc/libxslt-1.1.33/html/APIchunk9.html
/usr/share/doc/libxslt-1.1.33/html/APIconstructors.html
/usr/share/doc/libxslt-1.1.33/html/APIfiles.html
/usr/share/doc/libxslt-1.1.33/html/APIfunctions.html
/usr/share/doc/libxslt-1.1.33/html/APIsymbols.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/APIchunk0.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/APIconstructors.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/APIfiles.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/APIfunctions.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/APIsymbols.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/bugs.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/docs.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/downloads.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/exslt.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/help.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/index.html
/usr/share/doc/libxslt-1.1.33/html/EXSLT/intro.html
/usr/share/doc/libxslt-1.1.33/html/FAQ.html
/usr/share/doc/libxslt-1.1.33/html/Libxslt-Logo-180x168.gif
/usr/share/doc/libxslt-1.1.33/html/Libxslt-Logo-90x34.gif
/usr/share/doc/libxslt-1.1.33/html/bugs.html
/usr/share/doc/libxslt-1.1.33/html/contexts.gif
/usr/share/doc/libxslt-1.1.33/html/contribs.html
/usr/share/doc/libxslt-1.1.33/html/docbook.html
/usr/share/doc/libxslt-1.1.33/html/docs.html
/usr/share/doc/libxslt-1.1.33/html/downloads.html
/usr/share/doc/libxslt-1.1.33/html/extensions.html
/usr/share/doc/libxslt-1.1.33/html/help.html
/usr/share/doc/libxslt-1.1.33/html/html/book1.html
/usr/share/doc/libxslt-1.1.33/html/html/home.png
/usr/share/doc/libxslt-1.1.33/html/html/index.html
/usr/share/doc/libxslt-1.1.33/html/html/left.png
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-attributes.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-documents.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-extensions.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-extra.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-functions.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-imports.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-keys.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-lib.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-namespaces.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-numbersInternals.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-pattern.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-preproc.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-security.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-templates.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-transform.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-variables.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-xslt.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-xsltInternals.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-xsltexports.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-xsltlocale.html
/usr/share/doc/libxslt-1.1.33/html/html/libxslt-xsltutils.html
/usr/share/doc/libxslt-1.1.33/html/html/right.png
/usr/share/doc/libxslt-1.1.33/html/html/up.png
/usr/share/doc/libxslt-1.1.33/html/index.html
/usr/share/doc/libxslt-1.1.33/html/internals.html
/usr/share/doc/libxslt-1.1.33/html/intro.html
/usr/share/doc/libxslt-1.1.33/html/news.html
/usr/share/doc/libxslt-1.1.33/html/node.gif
/usr/share/doc/libxslt-1.1.33/html/object.gif
/usr/share/doc/libxslt-1.1.33/html/processing.gif
/usr/share/doc/libxslt-1.1.33/html/python.html
/usr/share/doc/libxslt-1.1.33/html/redhat.gif
/usr/share/doc/libxslt-1.1.33/html/smallfootonly.gif
/usr/share/doc/libxslt-1.1.33/html/stylesheet.gif
/usr/share/doc/libxslt-1.1.33/html/templates.gif
/usr/share/doc/libxslt-1.1.33/html/tutorial/libxslt_tutorial.c
/usr/share/doc/libxslt-1.1.33/html/tutorial/libxslttutorial.html
/usr/share/doc/libxslt-1.1.33/html/tutorial/libxslttutorial.xml
/usr/share/doc/libxslt-1.1.33/html/tutorial2/libxslt_pipes.c
/usr/share/doc/libxslt-1.1.33/html/tutorial2/libxslt_pipes.html
/usr/share/doc/libxslt-1.1.33/html/tutorial2/libxslt_pipes.xml
/usr/share/doc/libxslt-1.1.33/html/xslt.html
/usr/share/doc/libxslt-1.1.33/html/xsltproc.html
/usr/share/doc/libxslt-1.1.33/html/xsltproc2.html
/usr/share/man/man1/xsltproc.1.gz
/usr/share/man/man3/libexslt.3.gz
/usr/share/man/man3/libxslt.3.gz

%changelog
# let's skip this for now

