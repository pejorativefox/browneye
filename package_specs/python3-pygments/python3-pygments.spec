Name:       python3-pygments
Version:    2.6.1
Release:    1
Summary:    Pygments is a generic syntax highlighter
License:    Custom
Source0:    pygments-%{version}.tar.gz
Prefix:     /usr

%description
 It is a generic syntax highlighter suitable for use in code hosting, forums, wikis or other applications that need to prettify source code.

%prep
%setup -n pygments-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/bin/pygmentize
/usr/lib/python3.7/site-packages/Pygments-2.6.1.dev20200524-py3.7.egg-info/
/usr/lib/python3.7/site-packages/pygments/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2.6.1-1
- Initial rpm package
