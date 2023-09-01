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
/usr/include/libexslt/
/usr/include/libxslt/
/usr/share/man/
/usr/lib64/libexslt.so
/usr/lib64/libexslt.so.0
/usr/lib64/libexslt.so.0.8.20
/usr/lib64/libxslt.so
/usr/lib64/libxslt.so.1
/usr/lib64/libxslt.so.1.1.33
/usr/lib64/pkgconfig/libexslt.pc
/usr/lib64/pkgconfig/libxslt.pc
/usr/lib64/xsltConf.sh
/usr/share/aclocal/libxslt.m4
/usr/share/doc/libxslt-1.1.33/

%changelog
# let's skip this for now

