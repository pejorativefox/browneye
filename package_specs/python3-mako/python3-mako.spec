Name:       python3-mako
Version:    1.2.4
Release:    1
Summary:    A super-fast templating language that borrows the best ideas from the existing templating languages.
License:    MIT
Source0:    Mako-%{version}.tar.gz
Prefix:     /usr

%description
A super-fast templating language that borrows the best ideas from the existing templating languages.

%prep
%setup -n Mako-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/mako/
/usr/bin/mako-render
/usr/lib/python3.7/site-packages/Mako-1.2.4-py3.7.egg-info/

%changelog
* Thu Jun 15 2023 Chris Statzer <chris.statzer@qq.com> 1.2.4
- Initial rpm package
