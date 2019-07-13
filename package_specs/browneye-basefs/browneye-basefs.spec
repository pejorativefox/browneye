Name:       browneye-basefs
Version:    0.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /

%description
TODO

%prep

%build
mkdir -pv %{buildroot}/{dev,proc,sys,run,lib64,usr}
pushd %{buildroot}
ln -s lib64 lib
pushd usr
mkdir -pv lib64
ln -s lib64 lib
popd
popd

mknod -m 600 %{buildroot}/dev/console c 5 1
mknod -m 666 %{buildroot}/dev/null c 1 3

mkdir -v %{buildroot}/var/{log,mail,spool,run}
ln -sv /run %{buildroot}/var/run
ln -sv /run/lock %{buildroot}/var/lock
mkdir -pv %{buildroot}/var/{opt,cache,lib/{color,misc,locate},local}
touch /var/run/utmp
mkdir -pv %{buildroot}/tmp

%install


%files
/dev
/proc
/sys
/run
/lib64
/lib
/usr
/usr/lib64
/usr/lib
/dev/console
/dev/null
/var/log
/var/mail
/var/spool
/var/run
/var/run/utmp
/var/opt
/var/cache
/var/lib
/var/lib/color
/var/lib/misc
/var/lib/locate
/var/local
/tmp

%changelog
# let's skip this for now
