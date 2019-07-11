Name:       mpc
Version:    1.1.0
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
%configure --disable-static --docdir=/usr/share/doc/mpc-1.1.0
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/mpc.h
/usr/lib64/libmpc.la
/usr/lib64/libmpc.so
/usr/lib64/libmpc.so.3
/usr/lib64/libmpc.so.3.1.0
/usr/share/info/mpc.info.gz

%changelog
# let's skip this for now
