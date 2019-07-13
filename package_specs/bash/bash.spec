Name:       bash
Version:    5.0
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --docdir=/usr/share/doc/bash-5.0 \
           --without-bash-malloc            \
           --with-installed-readline

%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
pushd %{buildroot}/usr/bin
ln -s bash sh
popd

mkdir -pv %{buildroot}/etc/profile.d

cat > %{buildroot}/etc/profile << "EOF"
export PS1='(\h) \u:\w\$ '
alias ls='ls --color'
alias ll='ls -lash'

# Load profiles from /etc/profile.d
if test -d /etc/profile.d/; then
        for profile in /etc/profile.d/*.sh; do
                test -r "$profile" && . "$profile"
        done
        unset profile
fi

EOF




%files
/etc/profile.d
/etc/profile
/usr/bin/sh
/usr/bin/bash
/usr/bin/bashbug
/usr/include/bash/alias.h
/usr/include/bash/array.h
/usr/include/bash/arrayfunc.h
/usr/include/bash/assoc.h
/usr/include/bash/bashansi.h
/usr/include/bash/bashintl.h
/usr/include/bash/bashjmp.h
/usr/include/bash/bashtypes.h
/usr/include/bash/builtins.h
/usr/include/bash/builtins/bashgetopt.h
/usr/include/bash/builtins/builtext.h
/usr/include/bash/builtins/common.h
/usr/include/bash/builtins/getopt.h
/usr/include/bash/command.h
/usr/include/bash/config-bot.h
/usr/include/bash/config-top.h
/usr/include/bash/config.h
/usr/include/bash/conftypes.h
/usr/include/bash/dispose_cmd.h
/usr/include/bash/error.h
/usr/include/bash/externs.h
/usr/include/bash/general.h
/usr/include/bash/hashlib.h
/usr/include/bash/include/ansi_stdlib.h
/usr/include/bash/include/chartypes.h
/usr/include/bash/include/filecntl.h
/usr/include/bash/include/gettext.h
/usr/include/bash/include/maxpath.h
/usr/include/bash/include/memalloc.h
/usr/include/bash/include/ocache.h
/usr/include/bash/include/posixdir.h
/usr/include/bash/include/posixjmp.h
/usr/include/bash/include/posixstat.h
/usr/include/bash/include/posixtime.h
/usr/include/bash/include/posixwait.h
/usr/include/bash/include/shmbchar.h
/usr/include/bash/include/shmbutil.h
/usr/include/bash/include/shtty.h
/usr/include/bash/include/stat-time.h
/usr/include/bash/include/stdc.h
/usr/include/bash/include/systimes.h
/usr/include/bash/include/typemax.h
/usr/include/bash/include/unionwait.h
/usr/include/bash/jobs.h
/usr/include/bash/make_cmd.h
/usr/include/bash/pathnames.h
/usr/include/bash/quit.h
/usr/include/bash/shell.h
/usr/include/bash/sig.h
/usr/include/bash/siglist.h
/usr/include/bash/signames.h
/usr/include/bash/subst.h
/usr/include/bash/syntax.h
/usr/include/bash/unwind_prot.h
/usr/include/bash/variables.h
/usr/include/bash/version.h
/usr/include/bash/xmalloc.h
/usr/include/bash/y.tab.h
/usr/lib64/bash/Makefile.inc
/usr/lib64/bash/basename
/usr/lib64/bash/dirname
/usr/lib64/bash/fdflags
/usr/lib64/bash/finfo
/usr/lib64/bash/head
/usr/lib64/bash/id
/usr/lib64/bash/ln
/usr/lib64/bash/loadables.h
/usr/lib64/bash/logname
/usr/lib64/bash/mkdir
/usr/lib64/bash/mypid
/usr/lib64/bash/pathchk
/usr/lib64/bash/print
/usr/lib64/bash/printenv
/usr/lib64/bash/push
/usr/lib64/bash/realpath
/usr/lib64/bash/rmdir
/usr/lib64/bash/seq
/usr/lib64/bash/setpgid
/usr/lib64/bash/sleep
/usr/lib64/bash/strftime
/usr/lib64/bash/sync
/usr/lib64/bash/tee
/usr/lib64/bash/truefalse
/usr/lib64/bash/tty
/usr/lib64/bash/uname
/usr/lib64/bash/unlink
/usr/lib64/bash/whoami
/usr/lib64/pkgconfig/bash.pc
/usr/share/doc/bash-5.0/CHANGES
/usr/share/doc/bash-5.0/COMPAT
/usr/share/doc/bash-5.0/FAQ
/usr/share/doc/bash-5.0/INTRO
/usr/share/doc/bash-5.0/NEWS
/usr/share/doc/bash-5.0/POSIX
/usr/share/doc/bash-5.0/RBASH
/usr/share/doc/bash-5.0/README
/usr/share/doc/bash-5.0/bash.html
/usr/share/doc/bash-5.0/bashref.html
/usr/share/info/bash.info.gz
/usr/share/locale/af/LC_MESSAGES/bash.mo
/usr/share/locale/bg/LC_MESSAGES/bash.mo
/usr/share/locale/ca/LC_MESSAGES/bash.mo
/usr/share/locale/cs/LC_MESSAGES/bash.mo
/usr/share/locale/da/LC_MESSAGES/bash.mo
/usr/share/locale/de/LC_MESSAGES/bash.mo
/usr/share/locale/el/LC_MESSAGES/bash.mo
/usr/share/locale/en@boldquot/LC_MESSAGES/bash.mo
/usr/share/locale/en@quot/LC_MESSAGES/bash.mo
/usr/share/locale/eo/LC_MESSAGES/bash.mo
/usr/share/locale/es/LC_MESSAGES/bash.mo
/usr/share/locale/et/LC_MESSAGES/bash.mo
/usr/share/locale/fi/LC_MESSAGES/bash.mo
/usr/share/locale/fr/LC_MESSAGES/bash.mo
/usr/share/locale/ga/LC_MESSAGES/bash.mo
/usr/share/locale/gl/LC_MESSAGES/bash.mo
/usr/share/locale/hr/LC_MESSAGES/bash.mo
/usr/share/locale/hu/LC_MESSAGES/bash.mo
/usr/share/locale/id/LC_MESSAGES/bash.mo
/usr/share/locale/it/LC_MESSAGES/bash.mo
/usr/share/locale/ja/LC_MESSAGES/bash.mo
/usr/share/locale/lt/LC_MESSAGES/bash.mo
/usr/share/locale/nb/LC_MESSAGES/bash.mo
/usr/share/locale/nl/LC_MESSAGES/bash.mo
/usr/share/locale/pl/LC_MESSAGES/bash.mo
/usr/share/locale/pt/LC_MESSAGES/bash.mo
/usr/share/locale/pt_BR/LC_MESSAGES/bash.mo
/usr/share/locale/ro/LC_MESSAGES/bash.mo
/usr/share/locale/ru/LC_MESSAGES/bash.mo
/usr/share/locale/sk/LC_MESSAGES/bash.mo
/usr/share/locale/sl/LC_MESSAGES/bash.mo
/usr/share/locale/sr/LC_MESSAGES/bash.mo
/usr/share/locale/sv/LC_MESSAGES/bash.mo
/usr/share/locale/tr/LC_MESSAGES/bash.mo
/usr/share/locale/uk/LC_MESSAGES/bash.mo
/usr/share/locale/vi/LC_MESSAGES/bash.mo
/usr/share/locale/zh_CN/LC_MESSAGES/bash.mo
/usr/share/locale/zh_TW/LC_MESSAGES/bash.mo
/usr/share/man/man1/bash.1.gz
/usr/share/man/man1/bashbug.1.gz


%changelog
# let's skip this for now
