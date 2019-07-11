Name:       pkg-config
Version:    0.29.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --with-internal-glib --disable-host-tool \
           --docdir=/usr/share/doc/pkg-config-0.29.2
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/pkg-config
/usr/share/aclocal/pkg.m4
/usr/share/doc/pkg-config-0.29.2/pkg-config-guide.html
/usr/share/man/man1/pkg-config.1.gz


%changelog
# let's skip this for now
