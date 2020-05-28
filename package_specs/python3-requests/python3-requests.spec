Name:       python3-requests
Version:    2.23.0
Release:    1
Summary:    Requests: HTTP for Humans
License:    Apache2
Source0:    requests-v%{version}.tar.gz
Prefix:     /usr

%description
Requests is an elegant and simple HTTP library for Python, built for human beings.

%prep
%setup -n requests-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/requests-*
/usr/lib/python3.7/site-packages/requests/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2.23.0
- Initial rpm package
