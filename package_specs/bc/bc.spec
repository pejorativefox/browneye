Name:       bc
Version:    1.07.1
Release:    1
Summary:    Bc, an arbitrary precision numeric processing language. 
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
cat > bc/fix-libmath_h << "EOF"
#! /bin/bash
sed -e '1   s/^/{"/' \
    -e     's/$/",/' \
    -e '2,$ s/^/"/'  \
    -e   '$ d'       \
    -i libmath.h

sed -e '$ s/$/0}/' \
    -i libmath.h
EOF
sed -i -e '/flex/s/as_fn_error/: ;; # &/' configure
%configure --with-readline --mandir=/usr/share/man --infodir=/usr/share/info
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/bc
/usr/bin/dc
/usr/share/info/bc.info.gz
/usr/share/info/dc.info.gz
/usr/share/man/man1/bc.1.gz
/usr/share/man/man1/dc.1.gz


%changelog
# let's skip this for now
