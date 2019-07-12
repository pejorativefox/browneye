Name:       nspr
Version:    4.21
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
pushd nspr
%configure --enable-64bit
%make_build
popd

%install    
rm -rf %{buildroot}
pushd nspr
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/compile-et.pl
/usr/bin/nspr-config
/usr/bin/prerr.properties
/usr/include/md/_aix32.cfg
/usr/include/md/_aix64.cfg
/usr/include/md/_beos.cfg
/usr/include/md/_bsdi.cfg
/usr/include/md/_darwin.cfg
/usr/include/md/_dgux.cfg
/usr/include/md/_freebsd.cfg
/usr/include/md/_hpux32.cfg
/usr/include/md/_hpux64.cfg
/usr/include/md/_irix32.cfg
/usr/include/md/_irix64.cfg
/usr/include/md/_linux.cfg
/usr/include/md/_netbsd.cfg
/usr/include/md/_nto.cfg
/usr/include/md/_openbsd.cfg
/usr/include/md/_os2.cfg
/usr/include/md/_osf1.cfg
/usr/include/md/_qnx.cfg
/usr/include/md/_riscos.cfg
/usr/include/md/_scoos.cfg
/usr/include/md/_solaris.cfg
/usr/include/md/_symbian.cfg
/usr/include/md/_unixware.cfg
/usr/include/md/_unixware7.cfg
/usr/include/md/_win95.cfg
/usr/include/md/_winnt.cfg
/usr/include/nspr.h
/usr/include/obsolete/pralarm.h
/usr/include/obsolete/probslet.h
/usr/include/obsolete/protypes.h
/usr/include/obsolete/prsem.h
/usr/include/plarena.h
/usr/include/plarenas.h
/usr/include/plbase64.h
/usr/include/plerror.h
/usr/include/plgetopt.h
/usr/include/plhash.h
/usr/include/plstr.h
/usr/include/pratom.h
/usr/include/prbit.h
/usr/include/prclist.h
/usr/include/prcmon.h
/usr/include/prcountr.h
/usr/include/prcpucfg.h
/usr/include/prcvar.h
/usr/include/prdtoa.h
/usr/include/prenv.h
/usr/include/prerr.h
/usr/include/prerror.h
/usr/include/prinet.h
/usr/include/prinit.h
/usr/include/prinrval.h
/usr/include/prio.h
/usr/include/pripcsem.h
/usr/include/private/pprio.h
/usr/include/private/pprthred.h
/usr/include/private/prpriv.h
/usr/include/prlink.h
/usr/include/prlock.h
/usr/include/prlog.h
/usr/include/prlong.h
/usr/include/prmem.h
/usr/include/prmon.h
/usr/include/prmwait.h
/usr/include/prnetdb.h
/usr/include/prolock.h
/usr/include/prpdce.h
/usr/include/prprf.h
/usr/include/prproces.h
/usr/include/prrng.h
/usr/include/prrwlock.h
/usr/include/prshm.h
/usr/include/prshma.h
/usr/include/prsystem.h
/usr/include/prthread.h
/usr/include/prtime.h
/usr/include/prtpool.h
/usr/include/prtrace.h
/usr/include/prtypes.h
/usr/include/prvrsion.h
/usr/include/prwin16.h
/usr/lib64/libnspr4.a
/usr/lib64/libnspr4.so
/usr/lib64/libplc4.a
/usr/lib64/libplc4.so
/usr/lib64/libplds4.a
/usr/lib64/libplds4.so
/usr/lib64/pkgconfig/nspr.pc
/usr/share/aclocal/nspr.m4

%changelog
# let's skip this for now
