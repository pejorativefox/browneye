Name:       luit
Version:    1.1.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



%description
TODO

%prep
%setup -a 0

%build
sed -i -e "/D_XOPEN/s/5/6/" configure
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/luit
/usr/share/man/man1/luit.1.gz

%changelog
# let's skip this for now

