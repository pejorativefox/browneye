Name:       file
Version:    5.36
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
./configure --libdir=%{_libdir} --includedir=%{_includedir} --prefix=%{_prefix}
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/file
/usr/include/magic.h
/usr/lib64/libmagic.la
/usr/lib64/libmagic.so
/usr/lib64/libmagic.so.1
/usr/lib64/libmagic.so.1.0.0
/usr/share/man/man1/file.1.gz
/usr/share/man/man3/libmagic.3.gz
/usr/share/man/man4/magic.4.gz
/usr/share/misc/magic.mgc

%changelog
# let's skip this for now
