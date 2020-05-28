Name:       rust
Version:    1.31.1
Release:    2
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    rustc-1.31.1-x86_64-unknown-linux-gnu.tar.gz
Source1:    rust-std-1.31.1-x86_64-unknown-linux-gnu.tar.gz
Source2:    cargo-0.32.0-x86_64-unknown-linux-gnu.tar.gz

AutoReq: no

Requires: ld-linux-x86-64.so.2()(64bit), libc.so.6()(64bit), libdl.so.2()(64bit), libgcc_s.so.1()(64bit), libm.so.6()(64bit), libpthread.so.0()(64bit), librt.so.1()(64bit)


%description
TODO

%prep
rm -rf rust-1.31.1
mkdir rust-1.31.1
pushd rust-1.31.1
tar xf %{SOURCE0}
tar xf %{SOURCE1}
tar xf %{SOURCE2}
popd

%build

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/opt/rust
pushd rust-1.31.1
cp -r cargo-0.32.0-x86_64-unknown-linux-gnu/cargo/* %{buildroot}/opt/rust
cp -r rust-std-1.31.1-x86_64-unknown-linux-gnu/rust-std-x86_64-unknown-linux-gnu/* %{buildroot}/opt/rust
cp -r rustc-1.31.1-x86_64-unknown-linux-gnu/rustc/* %{buildroot}/opt/rust

mkdir -pv %{buildroot}/etc/profile.d
cat > %{buildroot}/etc/profile.d/rust_path.sh << "EOF"
export PATH=$PATH:/opt/rust/bin
EOF

popd


%files
/opt/rust/*
/etc/profile.d/rust_path.sh

%changelog
* Tue May 12 2020 Chris Statzer <chris.statzer@qq.com> 1.31.1
- Initial RPM
- Added path to default bash profile

