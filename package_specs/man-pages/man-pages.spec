Name:       man-pages
Version:    6.05.01
Release:    1
Summary:    The Linux man-pages
License:    Various
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The Linux man-pages project documents the Linux kernel and C library interfaces that are employed by user-space programs.

%prep
%setup -q

%build
rm -v man3/crypt*

%install
rm -rf %{buildroot}
%make_install prefix=/usr

%files
/usr/share/man

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

