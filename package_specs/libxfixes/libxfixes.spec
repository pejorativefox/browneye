Name:       libXfixes
Version:    6.0.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz



%description
TODO

%prep
%setup -a 0


%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/Xfixes.h
/usr/lib64/libXfixes.a
/usr/lib64/libXfixes.so
/usr/lib64/libXfixes.so.3
/usr/lib64/libXfixes.so.3.1.0
/usr/lib64/pkgconfig/xfixes.pc
/usr/share/man/man3/Xfixes.3.gz

%changelog
* Thu Aug 31 2023 Chris Statzer <chris.statzer@gmail.com> 6.0.1
- Version bump
