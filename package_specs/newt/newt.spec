Name:       newt
Version:    0.52.20
Release:    2
Summary:    Newt is a programming library for color text mode
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

%description
Newt is a programming library for color text mode

%package -n python2-newt
Summary: Newt python2 bindings
%description -n python2-newt
Newt python2 bindings

%prep
%setup -a 0

%build
sed -e 's/^LIBNEWT =/#&/' \
    -e '/install -m 644 $(LIBNEWT)/ s/^/#/' \
    -e 's/$(LIBNEWT)/$(LIBNEWTSONAME)/g' \
    -i Makefile.in
%configure --with-gpm-support
%make_build


%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/whiptail
/usr/include/newt.h
/usr/lib64/libnewt.so
/usr/lib64/libnewt.so.0.52
/usr/lib64/libnewt.so.0.52.20
/usr/lib64/pkgconfig/libnewt.pc
/usr/lib64/python3.7/site-packages/_snack.so
/usr/lib64/python3.7/site-packages/snack.py
/usr/share/locale/
/usr/share/man/man1/whiptail.1.gz

%files -n python2-newt
/usr/lib64/python2.7/site-packages/_snack.so
/usr/lib64/python2.7/site-packages/snack.py


%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 1.11.0-2
- packaged the python2 files in a sub package to prevent being pulled in deps

