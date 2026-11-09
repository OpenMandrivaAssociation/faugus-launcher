Name:           faugus-launcher
Version:        2.5.7
Release:        2
Summary:        Lightweight launcher for Windows games via UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson
BuildRequires:  pkgconfig(python3)

#Requires:  python-gobject
Requires:  python%{pyver}dist(requests)
#Requires:  python%{pyver}dist(icoextract)
#Requires:  python%{pyver}dist(pillow)
#Requires:  python%{pyver}dist(filelock)
Requires:  python%{pyver}dist(pillow-heif)
Requires:  python%{pyver}dist(vdf)
Requires:  python%{pyver}dist(psutil)
Requires:  typelib(Adw)
#Requires:  umu-launcher
#Requires:  imagemagick
#Requires:  typelib(Gtk) = 4.0
#Requires:  typelib(AyatanaAppIndicator3)

%description
A simple and lightweight app for running Windows games using UMU-Launcher

%prep
%autosetup -n %{name}-%{version} -p1
sed -i '1{/^#!/d}' faugus/launcher.py

%install -a
chmod 0644 %{buildroot}%{python3_sitelib}/faugus/backup.py \
           %{buildroot}%{python3_sitelib}/faugus/proton_downloader.py
chmod 0644 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/*.svg
ln -sf io.github.Faugus.faugus-launcher.svg \
       %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/faugus-launcher.svg

%files -f %{name}.lang
%license LICENSE
%{_bindir}/faugus-launcher
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/scalable/actions/*.svg
%{_datadir}/faugus-launcher/*

%{_datadir}/metainfo/*.xml
%{py_sitedir}/faugus
