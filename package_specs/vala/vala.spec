Name:       vala
Version:    0.56.11
Release:    1
Summary:    Vala programming language.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Vala is a new programming language that aims to bring modern programming language features to GNOME developers without imposing any additional runtime requirements and without using a different ABI compared to applications and libraries written in C. 

%prep
%setup

%build
%configure --disable-valadoc
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/
/usr/lib64/
/usr/share/
/usr/include/

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.40.8
- Initial RPM

