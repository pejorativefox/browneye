Name:       go-bin
Version:    1.12.7
Release:    1
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

%files
/opt/go/bin/go
/opt/go/bin/godoc
/opt/go/bin/gofmt
/opt/go/lib/time/README
/opt/go/lib/time/update.bash
/opt/go/lib/time/zoneinfo.zip

%changelog
# let's skip this for now
