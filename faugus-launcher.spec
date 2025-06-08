Name:           faugus-launcher
Version:        1.6.2
Release:        1
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires: python
Requires: python%{pyver}dist(gobject3)
Requires: python%{pyver}dist(pynput)
Requires: python%{pyver}dist(gi)
Requires: python%{pyver}dist(requests)
Requires: python%{pyver}dist(icoextract)
Requires: python%{pyver}dist(pillow)
Requires: umu-launcher
Requires: imagemagick
Requires: typelib(AppIndicator3)
Requires: typelib(AyatanaAppIndicator3)
Requires: python%{pyver}dist(vdf)
Requires: at-spi2-core
Requires: canberra-gtk3

%description
A simple and lightweight app for running Windows games using UMU-Launcher/UMU-Proton.

%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
install -Dm755 %{_builddir}/%{name}-%{version}/faugus_launcher.py %{buildroot}/%{_bindir}/faugus-launcher
install -Dm755 %{_builddir}/%{name}-%{version}/faugus_run.py %{buildroot}/%{_bindir}/faugus-run
install -Dm755 %{_builddir}/%{name}-%{version}/faugus_proton_manager.py %{buildroot}/%{_bindir}/faugus-proton-manager
install -Dm755 %{_builddir}/%{name}-%{version}/faugus_components.py %{buildroot}/%{_bindir}/faugus-components

install -Dm644 faugus-launcher.desktop %{buildroot}%{_datadir}/applications/faugus-launcher.desktop
install -Dm644 faugus-shortcut.desktop %{buildroot}%{_datadir}/applications/faugus-shortcut.desktop
install -Dm644 faugus-run.desktop %{buildroot}%{_datadir}/applications/faugus-run.desktop
install -Dm644 faugus-proton-manager.desktop %{buildroot}%{_datadir}/applications/faugus-proton-manager.desktop

install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-launcher.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-launcher.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-ea.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-ea.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-battlenet.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-battlenet.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-epic-games.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-epic-games.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-ubisoft-connect.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-ubisoft-connect.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-banner.png %{buildroot}/%{_datadir}/faugus-launcher/faugus-banner.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-notification.ogg %{buildroot}/%{_datadir}/faugus-launcher/faugus-notification.ogg

install -Dm644 assets/faugus-add-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/actions/faugus-add-symbolic.svg
install -Dm644 assets/faugus-exit-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/actions/faugus-exit-symbolic.svg
install -Dm644 assets/faugus-kill-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/actions/faugus-kill-symbolic.svg
install -Dm644 assets/faugus-play-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/actions/faugus-play-symbolic.svg
install -Dm644 assets/faugus-settings-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/actions/faugus-settings-symbolic.svg
install -Dm644 assets/faugus-stop-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/actions/faugus-stop-symbolic.svg

%files
%{_bindir}/faugus-launcher
%{_bindir}/faugus-run
%{_bindir}/faugus-proton-manager
%{_bindir}/faugus-components
%{_datadir}/applications/faugus-launcher.desktop
%{_datadir}/applications/faugus-shortcut.desktop
%{_datadir}/applications/faugus-run.desktop
%{_datadir}/applications/faugus-proton-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/faugus-launcher.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-ea.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-battlenet.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-epic-games.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-ubisoft-connect.png
%{_datadir}/faugus-launcher/faugus-banner.png
%{_datadir}/faugus-launcher/faugus-notification.ogg
%{_iconsdir}/hicolor/scalable/actions/faugus-add-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/faugus-exit-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/faugus-kill-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/faugus-play-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/faugus-stop-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/faugus-settings-symbolic.svg
