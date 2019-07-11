Name:       libcap
Version:    2.26
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed -i '/install.*STALIBNAME/d' libcap/Makefile
%make_build

%install    
rm -rf %{buildroot}
%make_install
chmod +x %{buildroot}/lib64/libcap.so.2.26

%files
/lib64/libcap.so
/lib64/libcap.so.2
/lib64/libcap.so.2.26
/sbin/capsh
/sbin/getcap
/sbin/getpcaps
/sbin/setcap
/usr/include/sys/capability.h
/usr/lib64/pkgconfig/libcap.pc
/usr/share/man/man1/capsh.1.gz
/usr/share/man/man3/cap_clear.3.gz
/usr/share/man/man3/cap_clear_flag.3.gz
/usr/share/man/man3/cap_compare.3.gz
/usr/share/man/man3/cap_copy_ext.3.gz
/usr/share/man/man3/cap_copy_int.3.gz
/usr/share/man/man3/cap_drop_bound.3.gz
/usr/share/man/man3/cap_dup.3.gz
/usr/share/man/man3/cap_free.3.gz
/usr/share/man/man3/cap_from_name.3.gz
/usr/share/man/man3/cap_from_text.3.gz
/usr/share/man/man3/cap_get_bound.3.gz
/usr/share/man/man3/cap_get_fd.3.gz
/usr/share/man/man3/cap_get_file.3.gz
/usr/share/man/man3/cap_get_flag.3.gz
/usr/share/man/man3/cap_get_pid.3.gz
/usr/share/man/man3/cap_get_proc.3.gz
/usr/share/man/man3/cap_init.3.gz
/usr/share/man/man3/cap_set_fd.3.gz
/usr/share/man/man3/cap_set_file.3.gz
/usr/share/man/man3/cap_set_flag.3.gz
/usr/share/man/man3/cap_set_proc.3.gz
/usr/share/man/man3/cap_size.3.gz
/usr/share/man/man3/cap_to_name.3.gz
/usr/share/man/man3/cap_to_text.3.gz
/usr/share/man/man3/capgetp.3.gz
/usr/share/man/man3/capsetp.3.gz
/usr/share/man/man3/libcap.3.gz
/usr/share/man/man8/getcap.8.gz
/usr/share/man/man8/setcap.8.gz


%changelog
# let's skip this for now
