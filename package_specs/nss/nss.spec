Name:       nss
Version:    3.42.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Patch:      nss-3.42.1-standalone-1.patch
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0
%patch -p1

%build
pushd nss
make -j1 BUILD_OPT=1                  \
  NSPR_INCLUDE_DIR=/usr/include/nspr  \
  USE_SYSTEM_ZLIB=1                   \
  ZLIB_LIBS=-lz                       \
  NSS_ENABLE_WERROR=0                 \
  $([ $(uname -m) = x86_64 ] && echo USE_64=1) \
  $([ -f /usr/include/sqlite3.h ] && echo NSS_USE_SYSTEM_SQLITE=1)
popd

%install    
rm -rf %{buildroot}

pushd dist
mkdir -pv %{buildroot}/usr/lib
mkdir -pv %{buildroot}/usr/include/nss
mkdir -pv %{buildroot}/usr/bin
mkdir -pv %{buildroot}/usr/lib/pkgconfig

install -v -m755 Linux*/lib/*.so              %{buildroot}/usr/lib
install -v -m644 Linux*/lib/{*.chk,libcrmf.a} %{buildroot}/usr/lib

install -v -m755 -d                           %{buildroot}/usr/include/nss
cp -v -RL {public,private}/nss/*              %{buildroot}/usr/include/nss
chmod -v 644                                  %{buildroot}/usr/include/nss/*

install -v -m755 Linux*/bin/{certutil,nss-config,pk12util} %{buildroot}/usr/bin

install -v -m644 Linux*/lib/pkgconfig/nss.pc  %{buildroot}/usr/lib/pkgconfig

rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/certutil
/usr/bin/nss-config
/usr/bin/pk12util
/usr/include/nss/alghmac.h
/usr/include/nss/base.h
/usr/include/nss/base64.h
/usr/include/nss/baset.h
/usr/include/nss/basicutil.h
/usr/include/nss/blake2b.h
/usr/include/nss/blapi.h
/usr/include/nss/blapit.h
/usr/include/nss/cert.h
/usr/include/nss/certdb.h
/usr/include/nss/certi.h
/usr/include/nss/certt.h
/usr/include/nss/certxutl.h
/usr/include/nss/chacha20poly1305.h
/usr/include/nss/ciferfam.h
/usr/include/nss/ck.h
/usr/include/nss/ckfw.h
/usr/include/nss/ckfwm.h
/usr/include/nss/ckfwtm.h
/usr/include/nss/ckhelper.h
/usr/include/nss/ckmd.h
/usr/include/nss/ckt.h
/usr/include/nss/cmmf.h
/usr/include/nss/cmmfi.h
/usr/include/nss/cmmfit.h
/usr/include/nss/cmmft.h
/usr/include/nss/cms.h
/usr/include/nss/cmsreclist.h
/usr/include/nss/cmst.h
/usr/include/nss/crmf.h
/usr/include/nss/crmfi.h
/usr/include/nss/crmfit.h
/usr/include/nss/crmft.h
/usr/include/nss/cryptohi.h
/usr/include/nss/cryptoht.h
/usr/include/nss/dev.h
/usr/include/nss/dev3hack.h
/usr/include/nss/devm.h
/usr/include/nss/devt.h
/usr/include/nss/devtm.h
/usr/include/nss/ec.h
/usr/include/nss/eccutil.h
/usr/include/nss/ecl-curve.h
/usr/include/nss/ecl-exp.h
/usr/include/nss/ecl.h
/usr/include/nss/eclt.h
/usr/include/nss/genname.h
/usr/include/nss/hasht.h
/usr/include/nss/hmacct.h
/usr/include/nss/jar-ds.h
/usr/include/nss/jar.h
/usr/include/nss/jarfile.h
/usr/include/nss/key.h
/usr/include/nss/keyhi.h
/usr/include/nss/keyi.h
/usr/include/nss/keyt.h
/usr/include/nss/keythi.h
/usr/include/nss/lgglue.h
/usr/include/nss/lowkeyi.h
/usr/include/nss/lowkeyti.h
/usr/include/nss/nss.h
/usr/include/nss/nssb64.h
/usr/include/nss/nssb64t.h
/usr/include/nss/nssbase.h
/usr/include/nss/nssbaset.h
/usr/include/nss/nssck.api
/usr/include/nss/nssckbi.h
/usr/include/nss/nssckepv.h
/usr/include/nss/nssckft.h
/usr/include/nss/nssckfw.h
/usr/include/nss/nssckfwc.h
/usr/include/nss/nssckfwt.h
/usr/include/nss/nssckg.h
/usr/include/nss/nssckmdt.h
/usr/include/nss/nssckt.h
/usr/include/nss/nssdev.h
/usr/include/nss/nssdevt.h
/usr/include/nss/nssilckt.h
/usr/include/nss/nssilock.h
/usr/include/nss/nsslocks.h
/usr/include/nss/nsslowhash.h
/usr/include/nss/nssoptions.h
/usr/include/nss/nsspki.h
/usr/include/nss/nsspkit.h
/usr/include/nss/nssrenam.h
/usr/include/nss/nssrwlk.h
/usr/include/nss/nssrwlkt.h
/usr/include/nss/nssutil.h
/usr/include/nss/ocsp.h
/usr/include/nss/ocspi.h
/usr/include/nss/ocspt.h
/usr/include/nss/ocspti.h
/usr/include/nss/p12.h
/usr/include/nss/p12plcy.h
/usr/include/nss/p12t.h
/usr/include/nss/pk11func.h
/usr/include/nss/pk11pqg.h
/usr/include/nss/pk11priv.h
/usr/include/nss/pk11pub.h
/usr/include/nss/pk11sdr.h
/usr/include/nss/pk11table.h
/usr/include/nss/pkcs11.h
/usr/include/nss/pkcs11f.h
/usr/include/nss/pkcs11n.h
/usr/include/nss/pkcs11ni.h
/usr/include/nss/pkcs11p.h
/usr/include/nss/pkcs11t.h
/usr/include/nss/pkcs11u.h
/usr/include/nss/pkcs11uri.h
/usr/include/nss/pkcs12.h
/usr/include/nss/pkcs12t.h
/usr/include/nss/pkcs1sig.h
/usr/include/nss/pkcs7t.h
/usr/include/nss/pki.h
/usr/include/nss/pki3hack.h
/usr/include/nss/pkim.h
/usr/include/nss/pkistore.h
/usr/include/nss/pkit.h
/usr/include/nss/pkitm.h
/usr/include/nss/pkix.h
/usr/include/nss/pkix_basicconstraintschecker.h
/usr/include/nss/pkix_build.h
/usr/include/nss/pkix_buildresult.h
/usr/include/nss/pkix_certchainchecker.h
/usr/include/nss/pkix_certsel.h
/usr/include/nss/pkix_certselector.h
/usr/include/nss/pkix_certstore.h
/usr/include/nss/pkix_checker.h
/usr/include/nss/pkix_comcertselparams.h
/usr/include/nss/pkix_comcrlselparams.h
/usr/include/nss/pkix_crlchecker.h
/usr/include/nss/pkix_crlsel.h
/usr/include/nss/pkix_crlselector.h
/usr/include/nss/pkix_ekuchecker.h
/usr/include/nss/pkix_error.h
/usr/include/nss/pkix_errorstrings.h
/usr/include/nss/pkix_expirationchecker.h
/usr/include/nss/pkix_lifecycle.h
/usr/include/nss/pkix_list.h
/usr/include/nss/pkix_logger.h
/usr/include/nss/pkix_namechainingchecker.h
/usr/include/nss/pkix_nameconstraintschecker.h
/usr/include/nss/pkix_ocspchecker.h
/usr/include/nss/pkix_params.h
/usr/include/nss/pkix_pl_aiamgr.h
/usr/include/nss/pkix_pl_basicconstraints.h
/usr/include/nss/pkix_pl_bigint.h
/usr/include/nss/pkix_pl_bytearray.h
/usr/include/nss/pkix_pl_cert.h
/usr/include/nss/pkix_pl_certpolicyinfo.h
/usr/include/nss/pkix_pl_certpolicymap.h
/usr/include/nss/pkix_pl_certpolicyqualifier.h
/usr/include/nss/pkix_pl_colcertstore.h
/usr/include/nss/pkix_pl_common.h
/usr/include/nss/pkix_pl_crl.h
/usr/include/nss/pkix_pl_crldp.h
/usr/include/nss/pkix_pl_crlentry.h
/usr/include/nss/pkix_pl_date.h
/usr/include/nss/pkix_pl_generalname.h
/usr/include/nss/pkix_pl_hashtable.h
/usr/include/nss/pkix_pl_httpcertstore.h
/usr/include/nss/pkix_pl_httpdefaultclient.h
/usr/include/nss/pkix_pl_infoaccess.h
/usr/include/nss/pkix_pl_ldapcertstore.h
/usr/include/nss/pkix_pl_ldapdefaultclient.h
/usr/include/nss/pkix_pl_ldaprequest.h
/usr/include/nss/pkix_pl_ldapresponse.h
/usr/include/nss/pkix_pl_ldapt.h
/usr/include/nss/pkix_pl_lifecycle.h
/usr/include/nss/pkix_pl_mem.h
/usr/include/nss/pkix_pl_monitorlock.h
/usr/include/nss/pkix_pl_mutex.h
/usr/include/nss/pkix_pl_nameconstraints.h
/usr/include/nss/pkix_pl_nsscontext.h
/usr/include/nss/pkix_pl_object.h
/usr/include/nss/pkix_pl_ocspcertid.h
/usr/include/nss/pkix_pl_ocsprequest.h
/usr/include/nss/pkix_pl_ocspresponse.h
/usr/include/nss/pkix_pl_oid.h
/usr/include/nss/pkix_pl_pk11certstore.h
/usr/include/nss/pkix_pl_pki.h
/usr/include/nss/pkix_pl_primhash.h
/usr/include/nss/pkix_pl_publickey.h
/usr/include/nss/pkix_pl_rwlock.h
/usr/include/nss/pkix_pl_socket.h
/usr/include/nss/pkix_pl_string.h
/usr/include/nss/pkix_pl_system.h
/usr/include/nss/pkix_pl_x500name.h
/usr/include/nss/pkix_policychecker.h
/usr/include/nss/pkix_policynode.h
/usr/include/nss/pkix_procparams.h
/usr/include/nss/pkix_resourcelimits.h
/usr/include/nss/pkix_results.h
/usr/include/nss/pkix_revchecker.h
/usr/include/nss/pkix_revocationchecker.h
/usr/include/nss/pkix_revocationmethod.h
/usr/include/nss/pkix_sample_modules.h
/usr/include/nss/pkix_signaturechecker.h
/usr/include/nss/pkix_store.h
/usr/include/nss/pkix_targetcertchecker.h
/usr/include/nss/pkix_tools.h
/usr/include/nss/pkix_trustanchor.h
/usr/include/nss/pkix_util.h
/usr/include/nss/pkix_validate.h
/usr/include/nss/pkix_valparams.h
/usr/include/nss/pkix_valresult.h
/usr/include/nss/pkix_verifynode.h
/usr/include/nss/pkixt.h
/usr/include/nss/portreg.h
/usr/include/nss/preenc.h
/usr/include/nss/sdb.h
/usr/include/nss/secasn1.h
/usr/include/nss/secasn1t.h
/usr/include/nss/seccomon.h
/usr/include/nss/secder.h
/usr/include/nss/secdert.h
/usr/include/nss/secdig.h
/usr/include/nss/secdigt.h
/usr/include/nss/secerr.h
/usr/include/nss/sechash.h
/usr/include/nss/secitem.h
/usr/include/nss/secmime.h
/usr/include/nss/secmod.h
/usr/include/nss/secmodi.h
/usr/include/nss/secmodt.h
/usr/include/nss/secmpi.h
/usr/include/nss/secoid.h
/usr/include/nss/secoidt.h
/usr/include/nss/secpkcs5.h
/usr/include/nss/secpkcs7.h
/usr/include/nss/secport.h
/usr/include/nss/secrng.h
/usr/include/nss/secutil.h
/usr/include/nss/sftkdbt.h
/usr/include/nss/shsign.h
/usr/include/nss/smime.h
/usr/include/nss/softkver.h
/usr/include/nss/softoken.h
/usr/include/nss/softoknt.h
/usr/include/nss/sqlite3.h
/usr/include/nss/ssl.h
/usr/include/nss/sslerr.h
/usr/include/nss/sslexp.h
/usr/include/nss/sslproto.h
/usr/include/nss/sslt.h
/usr/include/nss/templates.c
/usr/include/nss/utilmodt.h
/usr/include/nss/utilpars.h
/usr/include/nss/utilparst.h
/usr/include/nss/utilrename.h
/usr/include/nss/verref.h
/usr/include/nss/xconst.h
/usr/lib/libcrmf.a
/usr/lib/libfreebl3.chk
/usr/lib/libfreebl3.so
/usr/lib/libfreeblpriv3.chk
/usr/lib/libfreeblpriv3.so
/usr/lib/libgtest1.so
/usr/lib/libgtestutil.so
/usr/lib/libnss3.so
/usr/lib/libnssckbi.so
/usr/lib/libnssdbm3.chk
/usr/lib/libnssdbm3.so
/usr/lib/libnsssysinit.so
/usr/lib/libnssutil3.so
/usr/lib/libsmime3.so
/usr/lib/libsoftokn3.chk
/usr/lib/libsoftokn3.so
/usr/lib/libsqlite3.so
/usr/lib/libssl3.so
/usr/lib/pkgconfig/nss.pc

%changelog
# let's skip this for now
