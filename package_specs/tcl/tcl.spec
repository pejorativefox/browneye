Name:       tcl
Version:    8.6.13
Release:    1
Summary:    The tcl programming language
License:    Tcl/Tk
Source0:    %{name}%{version}-src.tar.gz
Prefix:     /usr
Patch0:     tcl-8.6.12-autopath.patch
Patch1:     tcl-8.6.12-conf.patch

%description
The tcl programming language

%prep
%setup -q -n tcl8.6.13
%patch0 -p1
%patch1 -p1

%build
export SRCDIR=$(pwd)
pushd unix
%configure
%make_build libdir=%{_libdir}

sed -e "s|$SRCDIR/unix|/usr/lib64|" \
    -e "s|$SRCDIR|/usr/include|"  \
    -i tclConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/tdbc1.1.5|/usr/lib64/tdbc1.1.5|" \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5/library|/usr/lib/64tcl8.6|" \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5|/usr/include|"            \
    -i pkgs/tdbc1.1.5/tdbcConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/itcl4.2.3|/usr/lib64/itcl4.2.3|" \
    -e "s|$SRCDIR/pkgs/itcl4.2.3/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/itcl4.2.3|/usr/include|"            \
    -i pkgs/itcl4.2.3/itclConfig.sh

unset SRCDIR
popd

%install
rm -rf %{buildroot}
pushd unix
%make_install
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
popd

%files -f ../../SOURCES/tcl.filelist

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

