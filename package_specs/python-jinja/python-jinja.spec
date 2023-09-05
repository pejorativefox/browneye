Name:       python3-jinja
Version:    3.1.2
Release:    1
Summary:    Python templating language
License:    Custom
Source0:    Jinja2-%{version}.tar.gz
Prefix:     /usr

%description
Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates.

%prep
%setup -n Jinja2-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.11/site-packages/jinja2/
/usr/lib/python3.11/site-packages/Jinja2-3.1.2-py3.11.egg-info/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 3.1.2-1
- Version bump

* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2.11.2
- Initial rpm package
