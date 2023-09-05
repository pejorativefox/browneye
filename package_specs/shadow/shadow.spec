Name:       shadow
Version:    4.13
Release:    1
Summary:    Shadow password format tools
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The shadow-utils package includes the necessary programs for converting UNIX password files to the shadow password format.

%prep
%setup -q -a0

%build
sed -i 's/groups$(EXEEXT) //' src/Makefile.in
find man -name Makefile.in -exec sed -i 's/groups\.1 / /'   {} \;
find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \;
find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \;

sed -i -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' \
       -e 's@/var/spool/mail@/var/mail@' etc/login.defs

%configure --with-{b,yes}crypt \
            --with-group-name-max-length=32
%make_build 

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
rm -rf %{buildroot}/etc/pam.d

%post
pwconv
grpconv

%files
/usr/bin/chage                                                                              
/usr/bin/chfn                                                                               
/usr/bin/chsh                                                                               
/usr/bin/expiry                                                                             
/usr/bin/faillog                                                                            
/usr/bin/getsubids                                                                          
/usr/bin/gpasswd                                                                            
/usr/bin/lastlog                                                                            
/usr/bin/login                                                                              
/usr/bin/newgidmap                                                                          
/usr/bin/newgrp                                                                             
/usr/bin/newuidmap                                                                          
/usr/bin/passwd                                                                             
/usr/bin/sg                                                                                 
/usr/bin/su                                                                                 
/usr/etc/limits                                                                             
/usr/etc/login.access                                                                       
/usr/etc/login.defs                                                                         
/usr/include/shadow/subid.h                                                                 
/usr/lib64/libsubid.a                                                                       
/usr/lib64/libsubid.so                                                                      
/usr/lib64/libsubid.so.4                                                                    
/usr/lib64/libsubid.so.4.0.0                                                                
/usr/sbin/chgpasswd                                                                         
/usr/sbin/chpasswd                                                                          
/usr/sbin/groupadd                                                                          
/usr/sbin/groupdel                                                                          
/usr/sbin/groupmems                                                                         
/usr/sbin/groupmod                                                                          
/usr/sbin/grpck                                                                             
/usr/sbin/grpconv                                                                           
/usr/sbin/grpunconv                                                                         
/usr/sbin/logoutd                                                                           
/usr/sbin/newusers     
/usr/sbin/nologin
/usr/sbin/pwck  
/usr/sbin/pwconv
/usr/sbin/pwunconv
/usr/sbin/useradd
/usr/sbin/userdel
/usr/sbin/usermod
/usr/sbin/vigr
/usr/sbin/vipw
/usr/share/locale/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 4.13-1
- Version bump

* Thu May 14 2020 Chris Statzer <chris.statzer@qq.com> 4.6-3
- Added post command to create /etc/shadow

