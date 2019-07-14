Name:       numactl
Version:    2.0.12
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/memhog
/usr/bin/migratepages
/usr/bin/migspeed
/usr/bin/numactl
/usr/bin/numademo
/usr/bin/numastat
/usr/include/numa.h
/usr/include/numacompat1.h
/usr/include/numaif.h
/usr/lib64/libnuma.la
/usr/lib64/libnuma.so
/usr/lib64/libnuma.so.1
/usr/lib64/libnuma.so.1.0.0
/usr/lib64/pkgconfig/numa.pc
/usr/share/man/man2/move_pages.2.gz
/usr/share/man/man3/numa.3.gz
/usr/share/man/man8/migratepages.8.gz
/usr/share/man/man8/migspeed.8.gz
/usr/share/man/man8/numactl.8.gz
/usr/share/man/man8/numastat.8.gz

%changelog
# let's skip this for now

