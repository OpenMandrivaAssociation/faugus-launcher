#define oversion 1.2-1

Name:           faugus-launcher
Version:        1.3.7
Release:        2
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires: python
Requires: python-gobject3
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

%description
A simple and lightweight app for running Windows games using UMU-Launcher/UMU-Proton.

%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-launcher.py %{buildroot}/%{_bindir}/faugus-launcher
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-gamepad.py %{buildroot}/%{_bindir}/faugus-gamepad
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-session %{buildroot}/%{_bindir}/faugus-session
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-run.py %{buildroot}/%{_bindir}/faugus-run
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-proton-manager.py %{buildroot}/%{_bindir}/faugus-proton-manager
install -Dm755 %{_builddir}/%{name}-%{version}/faugus-components.py %{buildroot}/%{_bindir}/faugus-components
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-launcher.desktop %{buildroot}/%{_datadir}/applications/faugus-launcher.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/faugus-shortcut.desktop %{buildroot}/%{_datadir}/applications/faugus-shortcut.desktop


install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-launcher.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-launcher.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-ea.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-ea.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-battlenet.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-battlenet.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-epic-games.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-epic-games.png
install -Dm644 %{_builddir}/%{name}-%{version}/assets/faugus-ubisoft-connect.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/faugus-ubisoft-connect.png

%files
%{_bindir}/faugus-launcher
%{_bindir}/faugus-run
%{_bindir}/faugus-gamepad
%{_bindir}/faugus-session
%{_bindir}/faugus-proton-manager
%{_bindir}/faugus-components
%{_datadir}/applications/faugus-launcher.desktop
%{_datadir}/applications/faugus-shortcut.desktop
%{_datadir}/icons/hicolor/256x256/apps/faugus-launcher.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-ea.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-battlenet.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-epic-games.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-ubisoft-connect.png
