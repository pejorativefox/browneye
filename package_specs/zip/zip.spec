Name:       zip
Version:    30
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}%{version}.tgz


%description
TODO

%prep
%setup -a 0 -n zip30

%build
make -f unix/Makefile generic_gcc

%install    
rm -rf %{buildroot}
#make prefix=/usr MANDIR=/usr/share/man/man1 -f unix/Makefile install DESTDIR=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/usr/bin
cp zip zipcloak zipnote zipsplit %{buildroot}/usr/bin

%files
/usr/bin/zip
/usr/bin/zipcloak
/usr/bin/zipnote
/usr/bin/zipsplit


%changelog
# let's skip this for now

