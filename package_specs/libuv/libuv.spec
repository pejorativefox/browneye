Name:       libuv
Version:    1.26.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-v%{version}.tar.gz



%description
TODO

%prep
%setup -a 0 -n libuv-v1.26.0


%build
sh autogen.sh
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/uv.h
/usr/include/uv/errno.h
/usr/include/uv/linux.h
/usr/include/uv/threadpool.h
/usr/include/uv/unix.h
/usr/include/uv/version.h
/usr/lib64/libuv.so
/usr/lib64/libuv.so.1
/usr/lib64/libuv.so.1.0.0
/usr/lib64/pkgconfig/libuv.pc

%changelog
# let's skip this for now
