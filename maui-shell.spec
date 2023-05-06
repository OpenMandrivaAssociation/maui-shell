%define libname %mklibname maui-shell
%define devname %mklibname -d maui-shell

#define snapshot 20220107

Name:		maui-shell
Version:	0.6.0
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	Maui Shell is a convergent shell for desktops, tablets, and phones.
Url:		https://github.com/Nitrux/maui-shell
Source0:	https://github.com/Nitrux/maui-shell/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

License:	 LGPL-3.0
Group:		Applications/Productivity/Shell/Maui
BuildRequires:  appstream
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
BuildRequires:  cmake(MauiMan)
BuildRequires:  cmake(MauiCore)
BuildRequires:  cmake(MauiKitFileBrowsing)
BuildRequires:  cmake(CaskServer)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:  cmake(Qt5WaylandCompositor)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:  qt5-qtbase-devel
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(Qt5QuickCompiler)
Requires:	%{libname} = %{EVRD}

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
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/cask
%{_bindir}/startcask
%{_bindir}/startcask-x11
%{_datadir}/wayland-sessions/cask.desktop
%{_datadir}/xsessions/cask-x11.desktop

%files -n %{libname}
%{_libdir}/libCaskAudio.so*
%{_libdir}/libCaskLib.so
%{_libdir}/libCaskNotifications.so*
%{_libdir}/qt5/qml/org/cask/audio/
%{_libdir}/qt5/qml/org/cask/notifications/
%{_libdir}/qt5/qml/org/maui/cask/

%files -n %{devname}
%{_includedir}/Cask/Audio/
%{_includedir}/Cask/Notifications/
%{_includedir}/Maui/Cask/
%{_libdir}/cmake/CaskAudio/
%{_libdir}/cmake/CaskLib/
%{_libdir}/cmake/CaskNotifications/
