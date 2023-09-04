Name:       dejagnu
Version:    1.6.3
Release:    1
Summary:    GNU Test framework
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
DejaGnu is a framework for testing other programs.

%prep
%setup

%build
mkdir build
pushd build
../configure --prefix=/usr --libdir=%{_libdir}
makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi
makeinfo --plaintext       -o doc/dejagnu.txt  ../doc/dejagnu.texi
popd

%install
rm -rf %{buildroot}
pushd build
install -v -dm755  %{buildroot}/usr/share/doc/dejagnu-1.6.3
install -v -m644   doc/dejagnu.{html,txt} %{buildroot}/usr/share/doc/dejagnu-1.6.3
%make_install
popd

%files
/usr/bin/dejagnu                                                                            
/usr/bin/runtest                                                                            
/usr/include/dejagnu.h  
/usr/share/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Initial RPM

