Name:       libogg
Version:    1.3.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -q -a 0 

%build
%configure  --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/libogg-1.3.3
%make_build

%install    
rm -rf %{buildroot}
%make_install

%files
/usr/include/ogg/*
/usr/lib64/*
/usr/share/doc/*
/usr/share/aclocal/*


%changelog
# let's skip this for now

