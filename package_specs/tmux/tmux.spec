Name:       tmux
Version:    3.3a
Release:    1
Summary:    tmux terminal multiplexer
License:    ISC
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

BuildRequires: libevent

%description
tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/tmux
/usr/share/man/man1/tmux.1.gz

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 3.3a
- Initial RPM

