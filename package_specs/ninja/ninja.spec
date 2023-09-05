Name:       ninja
Version:    1.11.1
Release:    1
Summary:    Ninja is a small build system with a focus on speed
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Ninja is a small build system with a focus on speed

%prep
%setup -q

%build
export NINJAJOBS=4
sed -i '/int Guess/a \
  int   j = 0;\
  char* jobs = getenv( "NINJAJOBS" );\
  if ( jobs != NULL ) j = atoi( jobs );\
  if ( j > 0 ) return j;\
' src/ninja.cc
python3 configure.py --bootstrap

%install
rm -rf %{buildroot}
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/usr/bin
mkdir -pv %{buildroot}/usr/share/bash-completion/
mkdir -pv %{buildroot}/usr/share/zsh/site-functions/
install -vm755 ninja %{buildroot}/usr/bin/
install -vDm644 misc/bash-completion %{buildroot}/usr/share/bash-completion/completions/ninja
install -vDm644 misc/zsh-completion  %{buildroot}/usr/share/zsh/site-functions/_ninja

%files
/usr/bin/ninja
/usr/share/bash-completion/completions/ninja
/usr/share/zsh/site-functions/_ninja

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.11.1
- Version bump
