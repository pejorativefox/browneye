Name:       terminator
Version:    1.91
Release:    1
Summary:    Terminator termnal emulator
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Terminator terminal emulator

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
python2 setup.py install --root %{buildroot}

%files
/usr/bin/remotinator
/usr/bin/terminator
/usr/bin/terminator.wrapper
/usr/lib/python2.7/site-packages/*
/usr/share/appdata/terminator.appdata.xml
/usr/share/applications/terminator.desktop
/usr/share/icons/
/usr/share/locale/*
/usr/share/man/man1/terminator.1.gz
/usr/share/man/man5/terminator_config.5.gz
/usr/share/pixmaps/terminator.png
/usr/share/terminator/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 42.0.2
- Initial rpm package
