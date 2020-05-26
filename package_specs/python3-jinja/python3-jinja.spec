Name:       python3-jinja
Version:    2.11.2
Release:    1
Summary:    Python templating language
License:    Custom
Source0:    jinja-%{version}.tar.gz
Prefix:     /usr

%description
Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates.

%prep
%setup -n jinja-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/Jinja2-2.11.2-py3.7.egg-info/
/usr/lib/python3.7/site-packages/jinja2/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2.11.2
- Initial rpm package
