Name:       texinfo
Version:    7.0.3
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

AutoReq: no

Requires: libc.so.6()(64bit), libncursesw.so.6()(64bit), perl >= 0:5.004


%description
TODO

%prep
%setup -q -a0

%build
sed -i '5481,5485 s/({/(\\{/' tp/Texinfo/Parser.pm
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/info
/usr/bin/install-info
/usr/bin/makeinfo
/usr/bin/pdftexi2dvi
/usr/bin/pod2texi
/usr/bin/texi2any
/usr/bin/texi2dvi
/usr/bin/texi2pdf
/usr/bin/texindex
/usr/lib64/
/usr/share/

%changelog
# let's skip this for now
