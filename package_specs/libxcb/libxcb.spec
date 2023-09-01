Name:       libxcb
Version:    1.13.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build 
sed -i "s/pthread-stubs//" configure
%configure --without-doxygen
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/
/usr/lib64/
/usr/share/

%changelog
# let's skip this for now
