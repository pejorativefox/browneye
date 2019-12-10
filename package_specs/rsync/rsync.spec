Name:       rsync
Version:    3.1.3
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
%configure --without-included-zlib
%make_build

%install
rm -rf %{buildroot}
%make_install

%post


%files
/usr/bin/rsync
/usr/share/man/man1/rsync.1.gz
/usr/share/man/man5/rsyncd.conf.5.gz

%changelog
# let's skip this for now
