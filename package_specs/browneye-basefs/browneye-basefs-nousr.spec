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
rm -rf %{buildroot}
mkdir -pv %{buildroot}/{dev,proc,sys,run,lib64,var,home}

pushd %{buildroot}
ln -s lib64 lib
#ln -s / usr

mknod -m 600 dev/console c 5 1
mknod -m 666 dev/null c 1 3

mkdir -pv var/{log,mail,spool}

ln -sv /run var/run
mkdir -pv run/lock
ln -sv /run/lock var/lock

mkdir -pv var/{opt,cache,lib/{color,misc,locate},local}
touch run/utmp
mkdir -pv tmp

popd





%install


%files
#/dev
#/usr
/proc
/sys
/run
/lib64
/lib
/dev/console
/dev/null
/var/log
/var/mail
/var/spool
/var/run
/run/utmp
/run/lock
/var/opt
/var/lock
/var/cache
#/var/lib
/var/lib/color
/var/lib/misc
/var/lib/locate
/var/local
/tmp

%changelog
# let's skip this for now
