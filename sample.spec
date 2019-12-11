Name:       dnf
Version:    4.2.6
Release:    1
Summary:    The DNF package manager
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Dandified YUM (DNF) is the next upcoming major version of YUM. It does package management using RPM, 
libsolv and hawkey libraries. For metadata handling and package downloads it utilizes librepo. 
To process and effectively handle the comps data it uses libcomps.

%prep
%setup

%build
mkdir build
pushd build
cmake .. -DPYTHON_DESIRED="3"
%make_build
popd

%install
rm -rf %{buildroot}
pushd  build
%make_install
popd

%files

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Added this sample to help with adding new packages.
