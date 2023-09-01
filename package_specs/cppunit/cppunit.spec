Name:       cppunit
Version:    1.15.1
Release:    1
Summary:    CppUnit is the C++ port of the famous JUnit framework for unit testing.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/DllPlugInTester
/usr/lib64/libcppunit-1.15.so.1
/usr/lib64/libcppunit-1.15.so.1.0.0
/usr/lib64/libcppunit.a
/usr/lib64/libcppunit.so
/usr/lib64/pkgconfig/cppunit.pc
/usr/share/doc/cppunit/AUTHORS
/usr/share/doc/cppunit/BUGS
/usr/share/doc/cppunit/CodingGuideLines.txt
/usr/share/doc/cppunit/FAQ
/usr/share/doc/cppunit/INSTALL
/usr/share/doc/cppunit/INSTALL-WIN32.txt
/usr/share/doc/cppunit/INSTALL-unix
/usr/include/cppunit/*

%changelog
* Wed May 13 2020 Chris Statzer <chris.statzer@qq.com> 1.15.1
- version bump for libdnf

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.14.0
- Initial RPM

