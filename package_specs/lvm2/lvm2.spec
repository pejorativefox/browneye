Name:       LVM2
Version:    2.03.05
Release:    1
Summary:    LVM library
License:    GPL3
Source0:    %{name}.%{version}.tgz
Prefix:     /usr

BuildRequires: libaio

%description
Provides logical volume management facilities on linux.

%prep
%setup -q -a0 -n LVM2.%{version}

%build
%configure --prefix=/usr --enable-pkgconfig
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/etc/lvm/lvm.conf
/etc/lvm/lvmlocal.conf
/etc/lvm/profile/cache-mq.profile
/etc/lvm/profile/cache-smq.profile
/etc/lvm/profile/command_profile_template.profile
/etc/lvm/profile/lvmdbusd.profile
/etc/lvm/profile/metadata_profile_template.profile
/etc/lvm/profile/thin-generic.profile
/etc/lvm/profile/thin-performance.profile
/etc/lvm/profile/vdo-small.profile
/usr/include/libdevmapper.h
/usr/lib/libdevmapper.so
/usr/lib/pkgconfig/devmapper.pc
/usr/lib64/libdevmapper.so.1.02
/usr/sbin/blkdeactivate
/usr/sbin/dmsetup
/usr/sbin/dmstats
/usr/sbin/fsadm
/usr/sbin/lvchange
/usr/sbin/lvconvert
/usr/sbin/lvcreate
/usr/sbin/lvdisplay
/usr/sbin/lvextend
/usr/sbin/lvm
/usr/sbin/lvmconfig
/usr/sbin/lvmdiskscan
/usr/sbin/lvmdump
/usr/sbin/lvmsadc
/usr/sbin/lvmsar
/usr/sbin/lvreduce
/usr/sbin/lvremove
/usr/sbin/lvrename
/usr/sbin/lvresize
/usr/sbin/lvs
/usr/sbin/lvscan
/usr/sbin/pvchange
/usr/sbin/pvck
/usr/sbin/pvcreate
/usr/sbin/pvdisplay
/usr/sbin/pvmove
/usr/sbin/pvremove
/usr/sbin/pvresize
/usr/sbin/pvs
/usr/sbin/pvscan
/usr/sbin/vgcfgbackup
/usr/sbin/vgcfgrestore
/usr/sbin/vgchange
/usr/sbin/vgck
/usr/sbin/vgconvert
/usr/sbin/vgcreate
/usr/sbin/vgdisplay
/usr/sbin/vgexport
/usr/sbin/vgextend
/usr/sbin/vgimport
/usr/sbin/vgimportclone
/usr/sbin/vgmerge
/usr/sbin/vgmknodes
/usr/sbin/vgreduce
/usr/sbin/vgremove
/usr/sbin/vgrename
/usr/sbin/vgs
/usr/sbin/vgscan
/usr/sbin/vgsplit
/usr/share/man/*



%changelog
# let's skip this for now
