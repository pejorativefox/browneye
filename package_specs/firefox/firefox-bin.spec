Name:       firefox-bin
Version:    68.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    firefox-%{version}.tar.bz2


%description
TODO

%prep
rm -rf firefox-bin
mkdir firefox-bin
pushd firefox-bin
tar xf %{SOURCE0}
popd
%build

%install    
rm -rf %{buildroot}
pushd firefox-bin
mkdir -pv %{buildroot}/opt
cp -r firefox %{buildroot}/opt
popd

%files
/opt/firefox/Throbber-small.gif
/opt/firefox/application.ini
/opt/firefox/browser/blocklist.xml
/opt/firefox/browser/chrome.manifest
/opt/firefox/browser/chrome/icons/default/default128.png
/opt/firefox/browser/chrome/icons/default/default16.png
/opt/firefox/browser/chrome/icons/default/default32.png
/opt/firefox/browser/chrome/icons/default/default48.png
/opt/firefox/browser/chrome/icons/default/default64.png
/opt/firefox/browser/crashreporter-override.ini
/opt/firefox/browser/features/formautofill@mozilla.org.xpi
/opt/firefox/browser/features/fxmonitor@mozilla.org.xpi
/opt/firefox/browser/features/screenshots@mozilla.org.xpi
/opt/firefox/browser/features/webcompat-reporter@mozilla.org.xpi
/opt/firefox/browser/features/webcompat@mozilla.org.xpi
/opt/firefox/browser/omni.ja
/opt/firefox/chrome.manifest
/opt/firefox/crashreporter
/opt/firefox/crashreporter.ini
/opt/firefox/defaults/pref/channel-prefs.js
/opt/firefox/dependentlibs.list
/opt/firefox/firefox
/opt/firefox/firefox-bin
/opt/firefox/firefox-bin.sig
/opt/firefox/firefox.sig
/opt/firefox/fonts/TwemojiMozilla.ttf
/opt/firefox/gmp-clearkey/0.1/libclearkey.so
/opt/firefox/gmp-clearkey/0.1/libclearkey.so.sig
/opt/firefox/gmp-clearkey/0.1/manifest.json
/opt/firefox/gtk2/libmozgtk.so
/opt/firefox/icons/updater.png
/opt/firefox/libfreeblpriv3.chk
/opt/firefox/libfreeblpriv3.so
/opt/firefox/liblgpllibs.so
/opt/firefox/libmozavcodec.so
/opt/firefox/libmozavutil.so
/opt/firefox/libmozgtk.so
/opt/firefox/libmozsandbox.so
/opt/firefox/libmozsqlite3.so
/opt/firefox/libmozwayland.so
/opt/firefox/libnspr4.so
/opt/firefox/libnss3.so
/opt/firefox/libnssckbi.so
/opt/firefox/libnssdbm3.chk
/opt/firefox/libnssdbm3.so
/opt/firefox/libnssutil3.so
/opt/firefox/libplc4.so
/opt/firefox/libplds4.so
/opt/firefox/libsmime3.so
/opt/firefox/libsoftokn3.chk
/opt/firefox/libsoftokn3.so
/opt/firefox/libssl3.so
/opt/firefox/libxul.so
/opt/firefox/libxul.so.sig
/opt/firefox/minidump-analyzer
/opt/firefox/omni.ja
/opt/firefox/pingsender
/opt/firefox/platform.ini
/opt/firefox/plugin-container
/opt/firefox/plugin-container.sig
/opt/firefox/precomplete
/opt/firefox/removed-files
/opt/firefox/update-settings.ini
/opt/firefox/updater
/opt/firefox/updater.ini

%changelog
# let's skip this for now

