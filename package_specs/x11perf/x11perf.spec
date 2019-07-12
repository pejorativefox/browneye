Name:       x11perf
Version:    1.6.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



%description
TODO

%prep
%setup -a 0

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/x11perf
/usr/bin/x11perfcomp
/usr/lib64/X11/x11perfcomp/Xmark
/usr/lib64/X11/x11perfcomp/fillblnk
/usr/lib64/X11/x11perfcomp/perfboth
/usr/lib64/X11/x11perfcomp/perfratio
/usr/share/man/man1/Xmark.1.gz
/usr/share/man/man1/x11perf.1.gz
/usr/share/man/man1/x11perfcomp.1.gz

%changelog
# let's skip this for now

