Name:       ruby
Version:    2.7.1
Release:    1
Summary:    Ruby programming language
License:    BSDL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Ruby programming language

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/bundle
/usr/bin/bundler
/usr/bin/erb
/usr/bin/gem
/usr/bin/irb
/usr/bin/racc
/usr/bin/racc2y
/usr/bin/rake
/usr/bin/rdoc
/usr/bin/ri
/usr/bin/ruby
/usr/bin/y2racc
/usr/include/ruby-2.7.0/
/usr/lib64/libruby-static.a
/usr/lib64/pkgconfig/ruby-2.7.pc
/usr/lib64/ruby/
/usr/share/man/
/usr/share/ri/2.7.0/

%changelog
* Fri Sep 04 2020 Chris Statzer <chris.statzer@qq.com> 2.7.1
- Initial RPM

