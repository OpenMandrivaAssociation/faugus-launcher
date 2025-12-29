Name:           faugus-launcher
Version:        1.11.8
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
%{_iconsdir}/hicolor/256x256/apps/faugus-mono.svg
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/faugus-launcher/*
%lang(af) %{_datadir}/locale/af/LC_MESSAGES/*.mo
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*.mo
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*.mo
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/*.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*.mo
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*.mo
%{_datadir}/metainfo/faugus-launcher.metainfo.xml
