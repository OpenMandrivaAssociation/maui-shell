%define git 20211230

Name:		maui-shell
Version:	0.%{git}
Release:	0.git.0
Summary:	Maui Shell is a convergent shell for desktops, tablets, and phones.
Url:		https://github.com/Nitrux/maui-shell
# Upstream still not provide any releases or tags. So until this happend use git.
# git clone --recursive https://github.com/Nitrux/maui-shell
# and then create archive %{name}-%{git}.xz
Source0:	%{name}-%{git}.tar.xz

License:	 LGPL-3.0
Group:		Applications/Productivity/Shell/Maui
BuildRequires:  appstream
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
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
#Requires:	%{libname} = %{EVRD}

%description
Maui Shell is a convergent shell for desktops, tablets, and phones.

Maui Shell is composed of two parts:

Cask is the shell container and elements templates, such as panels, popups, cards etc.
Zpace is the composer, which is the layout and places the windows or surfaces into the Cask container.

%prep
%autosetup -p1 -n %{name}-%{git}
%cmake  \
        -DENABLE_BSYMBOLICFUNCTIONS=OFF \
        -DQUICK_COMPILER=ON \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_EXPORT_NO_PACKAGE_REGISTRY=ON \
        -DCMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY=ON \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        "-GUnix Makefiles"

%build
%make_build

%install
%make_install -C build

%files
