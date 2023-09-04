Name:       glibc
Version:    2.38
Release:    1
Summary:    Provides the GNU glibc library
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

Provides: rtld(GNU_HASH)

%description
TODO
kluged to work around: https://www.linuxquestions.org/questions/slackware-14/bug-while-building-glibc-2-27-with-new-gcc-8-1-1-and-perl-5-28-0-a-4175632782/


%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/glibc-2.38-fhs-1.patch
patch -Np1 -i ../../SOURCES/glibc-2.38-memalign_fix-1.patch

mkdir build
pushd build
../configure --prefix=/usr --disable-werror --enable-kernel=3.2 \
             --enable-stack-protector=strong libc_cv_slibdir=/lib
TEXINFO_XS=omit make
popd

%install
#touch /root/rpmbuild/BUILD/glibc-%{version}/build/manual/libc.info # temp measure to stop docs from erroring
rm -rf %{buildroot}
pushd build
TEXINFO_XS=omit make -j1 install_root=$RPM_BUILD_ROOT install #MAKEINFO=true
popd
rm -vf %{buildroot}%{_infodir}/dir*


mkdir -pv %{buildroot}/etc
cat > %{buildroot}/etc/nsswitch.conf << "EOF"
# Begin /etc/nsswitch.conf

passwd: files
group: files
shadow: files

hosts: files dns
networks: files

protocols: files
services: files
ethers: files
rpc: files

# End /etc/nsswitch.conf
EOF

mkdir -pv %{buildroot}/etc/ld.so.conf.d/
cat >> %{buildroot}/etc/ld.so.conf << "EOF"
# Add an include directory
include /etc/ld.so.conf.d/*.conf

EOF
mkdir -pv /etc/ld.so.conf.d


%files -f ../../SOURCES/glibc.filelist

%changelog
# let's skip this for now
