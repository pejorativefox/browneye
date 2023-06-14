Name:       mandoc
Version:    1.14.6
Release:    1
Summary:    mandoc is an utility to format manual pages. 
License:    BSD
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
mandoc is an utility to format manual pages. 

%prep
%setup

%build
%configure
make mandoc

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
install -vm755 mandoc   %{buildroot}/usr/bin &&
mkdir -pv %{buildroot}/usr/share/man/man1
install -vm644 mandoc.1 %{buildroot}/usr/share/man/man1

%files
/usr/bin/mandoc
/usr/share/man/man1/mandoc.1.gz

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

