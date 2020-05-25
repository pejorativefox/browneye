Name:       python3-imagesize
Version:    1.1.0
Release:    1
Summary:    Analyzes various image formats
License:    MIT
Source0:    imagesize-%{version}.tar.gz
Prefix:     /usr

%description
This module analyzes JPEG/JPEG 2000/PNG/GIF/TIFF/SVG image headers and returns image size.

%prep
%setup -n imagesize_py-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/__pycache__/imagesize.cpython-37.pyc
/usr/lib/python3.7/site-packages/imagesize-1.1.0-py3.7.egg-info/
/usr/lib/python3.7/site-packages/imagesize.py

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.1.0-1
- Initial rpm package
