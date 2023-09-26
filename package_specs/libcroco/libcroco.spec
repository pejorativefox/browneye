Name:       libcroco
Version:    0.6.12
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -q

%build
%configure  --disable-static --enable-tee
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/croco-0.6-config
/usr/bin/csslint-0.6
/usr/include/libcroco-0.6/
/usr/lib64/libcroco-0.6.so
/usr/lib64/libcroco-0.6.so.3
/usr/lib64/libcroco-0.6.so.3.0.1
/usr/lib64/pkgconfig/libcroco-0.6.pc
/usr/share/gtk-doc/html/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.6.12-1
- Version bump

