Name:       pm-utils
Version:    1.4.1
Release:    1
Summary:    Power Management Utilitie
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The Power Management Utilities provide simple shell command line tools to suspend and hibernate the computer. They can be used to run user supplied scripts on suspend and resume. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/on_ac_power
/usr/bin/pm-is-supported
/usr/lib64/pkgconfig/pm-utils.pc
/usr/lib64/pm-utils/bin/pm-action
/usr/lib64/pm-utils/bin/pm-pmu
/usr/lib64/pm-utils/bin/pm-reset-swap
/usr/lib64/pm-utils/bin/service
/usr/lib64/pm-utils/defaults
/usr/lib64/pm-utils/functions
/usr/lib64/pm-utils/module.d/kernel
/usr/lib64/pm-utils/module.d/tuxonice
/usr/lib64/pm-utils/module.d/uswsusp
/usr/lib64/pm-utils/pm-functions
/usr/lib64/pm-utils/power.d/disable_wol
/usr/lib64/pm-utils/power.d/hal-cd-polling
/usr/lib64/pm-utils/power.d/harddrive
/usr/lib64/pm-utils/power.d/intel-audio-powersave
/usr/lib64/pm-utils/power.d/journal-commit
/usr/lib64/pm-utils/power.d/laptop-mode
/usr/lib64/pm-utils/power.d/pcie_aspm
/usr/lib64/pm-utils/power.d/readahead
/usr/lib64/pm-utils/power.d/sata_alpm
/usr/lib64/pm-utils/power.d/sched-powersave
/usr/lib64/pm-utils/power.d/wireless
/usr/lib64/pm-utils/power.d/xfs_buffer
/usr/lib64/pm-utils/sleep.d/00logging
/usr/lib64/pm-utils/sleep.d/00powersave
/usr/lib64/pm-utils/sleep.d/01grub
/usr/lib64/pm-utils/sleep.d/49bluetooth
/usr/lib64/pm-utils/sleep.d/55NetworkManager
/usr/lib64/pm-utils/sleep.d/75modules
/usr/lib64/pm-utils/sleep.d/90clock
/usr/lib64/pm-utils/sleep.d/94cpufreq
/usr/lib64/pm-utils/sleep.d/95led
/usr/lib64/pm-utils/sleep.d/98video-quirk-db-handler
/usr/lib64/pm-utils/sleep.d/99video
/usr/sbin/pm-hibernate
/usr/sbin/pm-powersave
/usr/sbin/pm-suspend
/usr/sbin/pm-suspend-hybrid
/usr/share/doc/pm-utils/HOWTO.hooks
/usr/share/doc/pm-utils/HOWTO.modules
/usr/share/doc/pm-utils/README
/usr/share/doc/pm-utils/README.debugging
/usr/share/doc/pm-utils/README.distributions

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 1.4.1
- Initial RPM

