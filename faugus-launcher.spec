#define oversion 1.2-1

Name:           faugus-launcher
Version:        1.3.7
Release:        8
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires: python
Requires: python-gobject3
Requires: python-pynput
Requires: python-gi
Requires: python-requests
Requires: python-icoextract
Requires: python-pillow 
Requires: umu-launcher
Requires: imagemagick
Requires: typelib(AppIndicator3)
Requires: lib64ayatana-appindicator3-gir0.1
Requires: python-vdf
Requires: at-spi2-core
Requires: lib64canberra-gtk3

%description
A simple and lightweight app for running Windows games using UMU-Launcher/UMU-Proton.

%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-launcher.py %{buildroot}/%{_bindir}/faugus-launcher
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-run.py %{buildroot}/%{_bindir}/faugus-run
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-proton-manager.py %{buildroot}/%{_bindir}/faugus-proton-manager
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-components.py %{buildroot}/%{_bindir}/faugus-components
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-gamepad.py %{buildroot}/%{_bindir}/faugus-gamepad
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-session %{buildroot}/%{_bindir}/faugus-session
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-launcher.desktop %{buildroot}/%{_datadir}/applications/faugus-launcher.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-shortcut.desktop %{buildroot}/%{_datadir}/applications/faugus-shortcut.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-run.desktop %{buildroot}/%{_datadir}/applications/faugus-run.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-proton-manager.desktop %{buildroot}/%{_datadir}/applications/faugus-proton-manager.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-session.desktop %{buildroot}/%{_datadir}/wayland-sessions/faugus-session.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-launcher.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-launcher.png
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-ea.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-ea.png
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-battlenet.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-battlenet.png
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-epic-games.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-epic-games.png
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-ubisoft-connect.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-ubisoft-connect.png
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-banner.png %{buildroot}/%{_datadir}/faugus-launcher/faugus-banner.png
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-notification.ogg %{buildroot}/%{_datadir}/faugus-launcher/faugus-notification.ogg

%files
%{_bindir}/faugus-launcher
%{_bindir}/faugus-run
%{_bindir}/faugus-proton-manager
%{_bindir}/faugus-components
%{_bindir}/faugus-gamepad
%{_bindir}/faugus-session
%{_datadir}/applications/faugus-launcher.desktop
%{_datadir}/applications/faugus-shortcut.desktop
%{_datadir}/applications/faugus-run.desktop
%{_datadir}/applications/faugus-proton-manager.desktop
%{_datadir}/wayland-sessions/faugus-session.desktop
%{_datadir}/icons/hicolor/256x256/apps/faugus-launcher.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-ea.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-battlenet.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-epic-games.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-ubisoft-connect.png
%{_datadir}/faugus-launcher/faugus-banner.png
%{_datadir}/faugus-launcher/faugus-notification.ogg
