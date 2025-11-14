Name:           faugus-launcher
Version:        1.10.4
Release:        1
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:	meson

BuildRequires:	gtk-update-icon-cache
Requires:	python-gobject
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(icoextract)
Requires:	python%{pyver}dist(pillow)
Requires:	python%{pyver}dist(filelock)
Requires:	python%{pyver}dist(vdf)
Requires:	python%{pyver}dist(psutil)
Requires:	umu-launcher
Requires:	imagemagick
Requires:	lib64ayatana-appindicator3_1

%description
A simple and lightweight app for running Windows games using UMU-Launcher/UMU-Proton.

%prep
%autosetup -n %{name}-%{version} -p1

%files
%license LICENSE
%{_bindir}/faugus-launcher
%{_bindir}/faugus-run
%{_bindir}/faugus-proton-manager
%{_bindir}/faugus-components
%{_bindir}/faugus-proton-downloader
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-mono.svg
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/faugus-launcher/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/metainfo/faugus-launcher.metainfo.xml
