Name:       m4
Version:    1.4.18
Release:    1
Summary:    M4 macro processor
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' lib/*.c
echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio-impl.h
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/m4
/usr/share/info/m4.info-1.gz
/usr/share/info/m4.info-2.gz
/usr/share/info/m4.info.gz
/usr/share/man/man1/m4.1.gz

%changelog
# let's skip this for now
