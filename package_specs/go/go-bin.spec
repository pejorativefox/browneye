Name:       go-bin
Version:    1.12.7
Release:    2
Summary:    TODO
License:    GPL3
Source0:    go1.12.7.linux-amd64.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -n go

%build 

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/opt/go
cp -r bin lib %{buildroot}/opt/go

mkdir -pv %{buildroot}/etc/profile.d
cat > %{buildroot}/etc/profile.d/go_path.sh << "EOF"
export PATH=$PATH:/opt/rust/bin
EOF

%files
/opt/go/*
/etc/profile.d/go_path.sh

%changelog
* Tue May 12 2020 Chris Statzer <chris.statzer@qq.com> 1.27.7
- Initial RPM
- Added path to default bash profile

