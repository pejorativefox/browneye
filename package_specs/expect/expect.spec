Name:       expect
Version:    5.45.4
Release:    1
Summary:    Automation tool
License:    Public Domain
Source0:    %{name}%{version}.tar.gz
Prefix:     /usr

%description
Expect is a tool for automating interactive applications.

%prep
%setup -n %{name}%{version}

%build
%configure  --with-tcl=/usr/lib   \
            --enable-shared         \
            --with-tclinclude=/usr/include
%make_build

%install
rm -rf %{buildroot}
%make_install
ln -svf expect5.45.4/libexpect5.45.4.so %{buildroot}/usr/lib
rm -rf %{buildroot}/usr/lib

%files
/usr/bin/autoexpect
/usr/bin/autopasswd
/usr/bin/cryptdir
/usr/bin/decryptdir
/usr/bin/dislocate
/usr/bin/expect
/usr/bin/ftp-rfc
/usr/bin/kibitz
/usr/bin/lpunlock
/usr/bin/mkpasswd
/usr/bin/multixterm
/usr/bin/passmass
/usr/bin/rftp
/usr/bin/rlogin-cwd
/usr/bin/timed-read
/usr/bin/timed-run
/usr/bin/tknewsbiff
/usr/bin/tkpasswd
/usr/bin/unbuffer
/usr/bin/weather
/usr/bin/xkibitz
/usr/bin/xpstat
/usr/include/expect.h
/usr/include/expect_comm.h
/usr/include/expect_tcl.h
/usr/include/tcldbg.h
/usr/lib64/expect5.45.4/libexpect5.45.4.so
/usr/lib64/expect5.45.4/pkgIndex.tcl
/usr/share/man/man1/autoexpect.1.gz
/usr/share/man/man1/cryptdir.1.gz
/usr/share/man/man1/decryptdir.1.gz
/usr/share/man/man1/dislocate.1.gz
/usr/share/man/man1/expect.1.gz
/usr/share/man/man1/kibitz.1.gz
/usr/share/man/man1/mkpasswd.1.gz
/usr/share/man/man1/multixterm.1.gz
/usr/share/man/man1/passmass.1.gz
/usr/share/man/man1/tknewsbiff.1.gz
/usr/share/man/man1/unbuffer.1.gz
/usr/share/man/man1/xkibitz.1.gz
/usr/share/man/man3/libexpect.3.gz

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 5.45.4
- Initial RPM

