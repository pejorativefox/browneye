Name:       popt
Version:    1.19
Release:    1
Summary:    popt command line option parsing library.
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
popt command line option parsing library.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/popt.h
/usr/lib64/libpopt.so
/usr/lib64/libpopt.so.0
/usr/lib64/libpopt.so.0.0.2
/usr/lib64/pkgconfig/popt.pc
/usr/share/locale/
/usr/share/man/man3/popt.3.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.19-1
- Version bump
