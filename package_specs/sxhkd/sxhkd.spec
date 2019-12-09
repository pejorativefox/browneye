Name:       sxhkd
Version:    0.6.1
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
%make_build 

%install
export PREFIX=/usr
rm -rf %{buildroot}
%make_install

%files
/usr/bin/sxhkd
/usr/share/doc/sxhkd/examples/background_shell/profile
/usr/share/doc/sxhkd/examples/background_shell/shell
/usr/share/doc/sxhkd/examples/background_shell/sxhkdrc
/usr/share/doc/sxhkd/examples/background_shell/xinitrc
/usr/share/doc/sxhkd/examples/notification/autostart
/usr/share/doc/sxhkd/examples/notification/pam_environment
/usr/share/doc/sxhkd/examples/notification/sxhkd_notify
/usr/share/doc/sxhkd/examples/notification/xinitrc
/usr/share/man/man1/sxhkd.1.gz

%changelog
# let's skip this for now
