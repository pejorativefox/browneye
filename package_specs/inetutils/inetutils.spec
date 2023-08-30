Name:       inetutils
Version:    1.9.4
Release:    1
Summary:    Collection of common network programs.
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Collection of common network programs.

%prep
%setup -q -a0

%build
%configure  --localstatedir=/var \
            --disable-logger     \
            --disable-whois      \
            --disable-rcp        \
            --disable-rexec      \
            --disable-rlogin     \
            --disable-rsh        \
            --disable-servers
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/
/usr/share/

%changelog
* Mon Jun 19 2023 Chris Statzer <chris.statzer@gmail.com> 1.9.4
- Removed the talk binary as it's no longer being built.
