Name:       cdrkit
Version:    1.1.11
Release:    1
Summary:    cdrkit is a collection of computer programs for CD and DVD authoring
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz
Patch0:     cdrkit-1.1.11-gcc10.patch 
AutoReq: no

%description
cdrkit is a collection of computer programs for CD and DVD authoring

%prep
%setup -a 0
%patch0 -p1

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX:PATH=/usr -DPREFIX=/usr
make
popd


%install    
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/cdda2mp3
/usr/bin/cdda2ogg
/usr/bin/devdump
/usr/bin/dirsplit
/usr/bin/genisoimage
/usr/bin/icedax
/usr/bin/isodebug
/usr/bin/isodump
/usr/bin/isoinfo
/usr/bin/isovfy
/usr/bin/pitchplay
/usr/bin/readmult
/usr/bin/readom
/usr/bin/wodim
/usr/sbin/netscsid
/usr/share/man/*

%changelog
# let's skip this for now

