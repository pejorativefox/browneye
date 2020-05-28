Name:       ntp
Version:    4.2.8p14
Release:    2
Summary:    NTP time sync daemon
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.gz
Source1:    ntp.conf
Source2:    ntpd.conf
Source3:    ntpd.service
Prefix:     /usr

%description
NTP Time sync daemon

%prep
%setup
sed -e 's/"(\\S+)"/"?([^\\s"]+)"?/' \
    -i scripts/update-leap/update-leap.in

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

mkdir -pv %{buildroot}/etc/finit.d/available
cp %{SOURCE1} %{buildroot}/etc
cp %{SOURCE2} %{buildroot}/etc/finit.d/available

mkdir -pv %{buildroot}/etc/service.d
cp %{SOURCE3} %{buildroot}/etc/service.d

%post
groupadd -g 87 ntp &&
useradd -c "Network Time Protocol" -d /var/lib/ntp -u 87 \
        -g ntp -s /bin/false ntp
install -v -o ntp -g ntp -d /var/lib/ntp

%files
/usr/bin/calc_tickadj
/usr/bin/ntp-keygen
/usr/bin/ntp-wait
/usr/bin/ntpd
/usr/bin/ntpdate
/usr/bin/ntpdc
/usr/bin/ntpq
/usr/bin/ntptime
/usr/bin/ntptrace
/usr/bin/sntp
/usr/bin/tickadj
/usr/bin/update-leap
/usr/share/doc/ntp/
/usr/share/doc/sntp/sntp.html
/usr/share/man/
/usr/share/ntp/lib/NTP/Util.pm
/etc/finit.d/available/ntpd.conf
/etc/ntp.conf
/etc/service.d/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 4.2.8p14-2
- Added default configuration and finit service

* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 4.2.8p14-1
- Initial RPM

