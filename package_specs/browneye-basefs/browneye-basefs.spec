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


%changelog
# let's skip this for now
