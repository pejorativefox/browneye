Name:       go-bin
Version:    1.20.5
Release:    2
Summary:    The go programming language (golang)
License:    GPL3
Source0:    go1.20.5.linux-amd64.tar.gz
Prefix:     /usr

%description
Go is a statically typed, compiled high-level programming language.

%prep
%setup -n go

%build 

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/opt/go
cp -r api bin doc lib doc misc pkg src %{buildroot}/opt/go

mkdir -pv %{buildroot}/etc/profile.d
cat > %{buildroot}/etc/profile.d/go_path.sh << "EOF"
export PATH=$PATH:/opt/go/bin
export GOROOT=/opt/go
EOF
rm %{buildroot}/opt/go/src/run.rc
rm %{buildroot}/opt/go/src/make.rc
rm %{buildroot}/opt/go/src/clean.rc
rm %{buildroot}/opt/go/src/all.rc

%files
/opt/go/*
/etc/profile.d/go_path.sh

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 1.20.5
- Version bump

* Tue May 12 2020 Chris Statzer <chris.statzer@qq.com> 1.12.7
- Initial RPM
- Added path to default bash profile

