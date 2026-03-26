Name:           faugus-launcher
Version:        1.17.1
Release:        1
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/%name
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:    meson

BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson
BuildRequires:  gettext

Requires:	python-gobject
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(icoextract)
Requires:	python%{pyver}dist(pillow)
Requires:	python%{pyver}dist(filelock)
Requires:	python%{pyver}dist(vdf)
Requires:	python%{pyver}dist(psutil)
Requires:	umu-launcher
Requires:	imagemagick
Requires:   typelib(AyatanaAppIndicator3)
Requires:	canberra-gtk3

%description
%summary

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%name
%{_bindir}/faugus-run
%{_bindir}/faugus-proton-manager
%{_bindir}/faugus-shortcut
%{_datadir}/applications/faugus*.desktop
%{_iconsdir}/hicolor/256x256/apps/faugus*.png
%{_iconsdir}/hicolor/256x256/apps/io.github.Faugus.%name.png
%{_iconsdir}/hicolor/256x256/apps/faugus-mono.svg
%{_iconsdir}/hicolor/scalable/actions/faugus*.svg
%{_datadir}/%name/*
%{_datadir}/metainfo/%name.metainfo.xml
%{py_sitedir}/faugus
