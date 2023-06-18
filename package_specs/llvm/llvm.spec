Name:       llvm
Version:    16.0.5
Release:    1
Summary:    The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. 
License:    UIUC
Source0:    %{name}-%{version}.src.tar.xz
Source1:    llvm-third-party.src.tar.xz
Source2:    llvm-cmake.src.tar.xz
Prefix:     /usr

%description
The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. The name "LLVM" itself is not an acronym; it is the full name of the project.

%prep
%setup -a 0 -n %{name}-%{version}.src
%setup -a 1 -T -D -n %{name}-%{version}.src
%setup -a 2 -T -D -n %{name}-%{version}.src

%build
mv llvm-third-party.src third-party

sed '/LLVM_THIRD_PARTY_DIR/s@../third-party@third-party@' \
    -i cmake/modules/HandleLLVMOptions.cmake

sed '/LLVM_COMMON_CMAKE_UTILS/s@../cmake@llvm-cmake.src@'          \
    -i CMakeLists.txt      

mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=/usr               \
      -DLLVM_ENABLE_FFI=ON                      \
      -DCMAKE_BUILD_TYPE=Release                \
      -DLLVM_BUILD_LLVM_DYLIB=ON                \
      -DLLVM_LINK_LLVM_DYLIB=ON                 \
      -DLLVM_ENABLE_RTTI=ON                     \
      -DLLVM_TARGETS_TO_BUILD="host;AMDGPU;BPF" \
      -DLLVM_BINUTILS_INCDIR=/usr/include       \
      -DLLVM_INCLUDE_BENCHMARKS=OFF             \
      -DCLANG_DEFAULT_PIE_ON_LINUX=ON           \
      -Wno-dev -G Ninja ..                      
ninja
popd


%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install 
popd

%files
/usr/bin/
/usr/include/llvm/
/usr/include/llvm-c/
/usr/lib/
/usr/share/opt-viewer/

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 16.0.5
- Initial RPM

