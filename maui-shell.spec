%define libname %mklibname maui-shell
%define devname %mklibname -d maui-shell

#define snapshot 20220107

Name:		maui-shell
Version:	0.6.6
Release:	3.20241022
Summary:	Maui Shell is a convergent shell for desktops, tablets, and phones.
Url:		https://github.com/Nitrux/maui-shell
#Source0:	https://github.com/Nitrux/maui-shell/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Use git to pull qt6
Source0:  maui-shell-master.tar.gz
#Patch0:   fix-build-with-mauikit-and-mauiman-3.0.2.patch

License:	 LGPL-3.0
Group:		Applications/Productivity/Shell/Maui
BuildRequires:  appstream
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiMan4)
BuildRequires:  cmake(MauiCore)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(CaskServer)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Package)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:  cmake(Qt6WaylandCompositor)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:  cmake(KDED)
#BuildRequires:  qt5-qtbase-devel
#BuildRequires:	qt5-qtgraphicaleffects
#BuildRequires:	qt5-qtdeclarative
#BuildRequires:	qt5-qtquickcontrols2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:	cmake(KF6Activities)
BuildRequires:	cmake(KF6ActivitiesStats)
BuildRequires:	cmake(KF6Completion)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:	cmake(KF6ItemViews)
#BuildRequires:	cmake(KF6Init)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Prison)
BuildRequires:	cmake(KF6Solid)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Runner)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Wallet)
#BuildRequires:  cmake(KF6Wayland)
BuildRequires:	cmake(KF6WidgetsAddons)
Requires:	%{libname} = %{EVRD}

Requires: qml(org.mauicore.power)
Requires: cask-server

Requires: bluedevil
Requires: kirigami2
#Requires: %{_lib}KF5Kirigami2_5
#Requires: plasma-framework
#Requires: plasma-nm
#Requires: plasma-pa
#Requires: qml(org.kde.bluezqt)
#Requires: qt5-qtquickcontrols2
#Requires: qt5-qtmultimedia
#Requires: qt5-qtwayland

%description
Maui Shell is a convergent shell for desktops, tablets, and phones.

Maui Shell is composed of two parts:

Cask is the shell container and elements templates, such as panels, popups, cards etc.
Zpace is the composer, which is the layout and places the windows or surfaces into the Cask container.

%package -n %{libname}
Summary:	Library files for maui-shell
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library files for mauikit-shell

%package -n %{devname}
Summary:	Development files for mauikit-shell
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for mauikit-shell

%prep
%autosetup -p1 -n %{name}-master
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc %{_datadir}/wallpapers/Cask/LICENSE
%{_bindir}/cask
%{_bindir}/cask_session
%{_bindir}/startcask-wayland
%{_sysconfdir}/xdg/autostart/cask.desktop
%{_datadir}/applications/cask.desktop
%{_datadir}/wayland-sessions/cask-session.desktop
%{_datadir}/wallpapers/Cask/maui_shell_dev_bg.png

%files -n %{libname}
%{_libdir}/libCaskLib.so
%{_libdir}/libCaskPolkit.so
%{_libdir}/libexec/cask-dbus-run-session-if-needed
%{_libdir}/libexec/cask-sourceenv.sh
%{_libdir}/qt5/qml/org/cask/polkit/
%{_libdir}/qt5/qml/org/maui/cask/

%files -n %{devname}
%{_includedir}/Cask/Polkit/
%{_includedir}/Cask/Power/
%{_includedir}/Maui/Cask/
%{_libdir}/cmake/CaskLib/
%{_libdir}/cmake/CaskPolkit/
