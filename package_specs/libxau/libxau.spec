Name:       libxau
Version:    1.0.11
Release:    1
Summary:    X11 authorisation library
License:    GPL3
Source0:    libXau-%{version}.tar.xz
Prefix:     /usr

%description
X11 authorisation library

%prep
%setup -q -n libXau-%{version}

%build 
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xauth.h
/usr/lib64/libXau.a
/usr/lib64/libXau.so
/usr/lib64/libXau.so.6
/usr/lib64/libXau.so.6.0.0
/usr/lib64/pkgconfig/xau.pc
/usr/share/man/man3/Xau.3.gz
/usr/share/man/man3/XauDisposeAuth.3.gz
/usr/share/man/man3/XauFileName.3.gz
/usr/share/man/man3/XauGetAuthByAddr.3.gz
/usr/share/man/man3/XauGetBestAuthByAddr.3.gz
/usr/share/man/man3/XauLockAuth.3.gz
/usr/share/man/man3/XauReadAuth.3.gz
/usr/share/man/man3/XauUnlockAuth.3.gz
/usr/share/man/man3/XauWriteAuth.3.gz


%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.0.11-1
- Version bump
