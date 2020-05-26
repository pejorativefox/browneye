Name:       python3-docutils
Version:    0.16
Release:    1
Summary:    Python docutils module
License:    TODO
Source0:    docutils-%{version}.tar.gz
Prefix:     /usr

%description
Docutils is an open-source text processing system for processing plaintext documentation into useful formats, such as HTML, LaTeX, man-pages, open-document or XML. 

%prep
%setup -n docutils-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/bin/rst2html.py
/usr/bin/rst2html4.py
/usr/bin/rst2html5.py
/usr/bin/rst2latex.py
/usr/bin/rst2man.py
/usr/bin/rst2odt.py
/usr/bin/rst2odt_prepstyles.py
/usr/bin/rst2pseudoxml.py
/usr/bin/rst2s5.py
/usr/bin/rst2xetex.py
/usr/bin/rst2xml.py
/usr/bin/rstpep2html.py
/usr/lib/python3.7/site-packages/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 0.16-1
- Initial rpm package
