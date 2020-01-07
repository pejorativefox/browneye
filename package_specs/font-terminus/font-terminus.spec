Name:       font-terminus
Version:    4.48
Release:    1
Summary:    Terminus Font is a clean, fixed width bitmap font.
License:    GPL3
Prefix:     /usr
Source0:    terminus-font-%{version}.tar.gz


%description
Terminus Font is a clean, fixed width bitmap font

%prep
%setup -n terminus-font-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%post
fc-cache -f -v

%files
/usr/share/consolefonts/*
/usr/share/fonts/terminus/*

%changelog
# let's skip this for now

