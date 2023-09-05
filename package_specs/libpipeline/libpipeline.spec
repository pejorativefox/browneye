Name:       libpipeline
Version:    1.5.7
Release:    1
Summary:    Subprocess manipulation library
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
C library for manipulating pipelines of subprocesses

%prep
%setup -q -a0

%build
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/pipeline.h
/usr/lib64/libpipeline.so
/usr/lib64/libpipeline.so.1
/usr/lib64/pkgconfig/libpipeline.pc
/usr/lib64/libpipeline.so.%{version}
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.5.7-1
- Version bump
