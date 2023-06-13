Name:       
Version:    
Release:    1
Summary:    
License:    
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description


%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

