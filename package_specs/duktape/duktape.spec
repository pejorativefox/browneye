Name:       duktape
Version:    2.7.0
Release:    1
Summary:    Lightweight JS engine
License:    MIT
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Lightweight JS engine

%prep
%setup

%build
sed -i 's/-Os/-O2/' Makefile.sharedlibrary
%make_build -f Makefile.sharedlibrary INSTALL_PREFIX=/usr

%install
rm -rf %{buildroot}
%make_install -f Makefile.sharedlibrary INSTALL_PREFIX=/usr

%files
/usr/lib
/usr/include 

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

