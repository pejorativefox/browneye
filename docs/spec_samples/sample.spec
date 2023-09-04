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
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Initial RPM

