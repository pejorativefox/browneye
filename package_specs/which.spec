Name:       which
Version:    2.21
Release:    1
Summary:    Provides the GNU which executable
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
which-2.21.tar.gz 

%prep
%setup -q -a0

%build
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/which
/usr/share/info/dir
/usr/share/info/which.info.gz
/usr/share/man/man1/which.1.gz
%changelog
# let's skip this for now
