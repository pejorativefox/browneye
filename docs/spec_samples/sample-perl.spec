Name:       perl-
Version:    
Release:    1
Summary:    
License:    
Source0:    -%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description


%prep
%setup -n -%{version}

%build
perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.44
- Initial RPM

