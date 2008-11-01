#
# TODO:
# - update files
# - separate applets and plugins into subpackages
# - make applets subpackage suggest all the applets
#
Summary:	Extra applets and plugins for awn
Summary(pl.UTF-8):	Dodatkowe applety i wtyczki dla awn
Name:		avant-window-navigator-extras
Version:	0.2.6
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://launchpad.net/awn-extras/0.2/%{version}/+download/awn-extras-applets-%{version}.tar.gz
# Source0-md5:	a02a7d82f086db96bca35d7865d2fa03
URL:		https://launchpad.net/awn-extras/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	avant-window-navigator-devel >= %{version}
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gnome-doc-utils >= 0.7.1
BuildRequires:	gnome-menus-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgtop-devel >= 2.0
BuildRequires:	libnotify-devel
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:  libsexy-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python-pyalsa
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	python-pyalsa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		awn_appletsdir	%{_libdir}/awn/applets

%description
Extra applets and plugins for awn.

%description -l pl.UTF-8
Dodatkowe applety i wtyczki dla awn.

%package -n avant-window-navigator-core-applets
Summary:	Core applets for awn
Summary(pl.UTF-8):	Kluczowe aplety dla awn
Group:		X11/Applications
Requires:	avant-window-navigator = %{version}

%description -n avant-window-navigator-core-applets
Core applets for awn.

%description -n avant-window-navigator-core-applets -l pl.UTF-8
Kluczowe aplety dla awn.

%package -n avant-window-navigator-plugins
Summary:	Pluggins for awn
Summary(pl.UTF-8):	Wtyczki dla awn
Group:		X11/Applications
Requires:	avant-window-navigator = %{version}

%description -n avant-window-navigator-plugins
Pluggins for awn.

%description -n avant-window-navigator-plugins -l pl.UTF-8
Wtyczki dla awn.

%prep
%setup -q -n awn-extras-applets-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install switcher.schemas
%gconf_schema_install awnsystemmonitor.schemas
%gconf_schema_install filebrowser.schemas
%gconf_schema_install notification-daemon.schemas
%gconf_schema_install trash.schemas

%preun
%gconf_schema_uninstall switcher.schemas
%gconf_schema_uninstall awnsystemmonitor.schemas
%gconf_schema_uninstall filebrowser.schemas
%gconf_schema_uninstall notification-daemon.schemas
%gconf_schema_uninstall trash.schemas

%files -n avant-window-navigator-core-applets
%defattr(644,root,root,755)
%dir %{_datadir}/awn-core-applets

%dir %{awn_appletsdir}/awnnotificationdaemon
%attr(755,root,root) %{awn_appletsdir}/awnnotificationdaemon/awnnotificationdaemon.so
%{awn_appletsdir}/awnnotificationdaemon.desktop
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service

%dir %{awn_appletsdir}/awnsystemmonitor
%attr(755,root,root) %{awn_appletsdir}/awnsystemmonitor/awnsystemmonitor.so
%{awn_appletsdir}/awn-system-monitor.desktop
%{_sysconfdir}/gconf/schemas/awnsystemmonitor.schemas

%{awn_appletsdir}/battery-applet
%{awn_appletsdir}/battery-applet.desktop

%{awn_appletsdir}/BlingSwitcher
%{awn_appletsdir}/PySwitcher.desktop

%dir %{awn_appletsdir}/clock
%attr(755,root,root) %{awn_appletsdir}/clock/clock.so
%{awn_appletsdir}/clock.desktop

%dir %{awn_appletsdir}/filebrowser
%attr(755,root,root) %{awn_appletsdir}/filebrowser/filebrowser.so
%{awn_appletsdir}/filebrowser.desktop
%{_datadir}/awn-core-applets/filebrowser.svg
%{_sysconfdir}/gconf/schemas/filebrowser.schemas

%{awn_appletsdir}/gmail
%{awn_appletsdir}/awngmail.desktop

%dir %{awn_appletsdir}/mainmenu
%attr(755,root,root) %{awn_appletsdir}/mainmenu/mainmenu.so
%{awn_appletsdir}/main-menu.desktop

%{awn_appletsdir}/media-control
%{awn_appletsdir}/media-control.desktop
%{awn_appletsdir}/media-icon-*
%{awn_appletsdir}/medialogo*.desktop

%dir %{awn_appletsdir}/notification-area
%attr(755,root,root) %{awn_appletsdir}/notification-area/notification-area.so
%{awn_appletsdir}/notification-area.desktop
%{_datadir}/awn-core-applets/notification.svg

%{awn_appletsdir}/quit-applet
%{awn_appletsdir}/quit-applet.desktop

%dir %{awn_appletsdir}/separator
%attr(755,root,root) %{awn_appletsdir}/separator/separator.so
%{awn_appletsdir}/separator.desktop
%{_datadir}/awn-core-applets/separator.svg

%{awn_appletsdir}/showdesktop
%{awn_appletsdir}/showdesktop.desktop

%{awn_appletsdir}/stacks
%{awn_appletsdir}/stacks.desktop

%dir %{awn_appletsdir}/switcher
%attr(755,root,root) %{awn_appletsdir}/switcher/switcher.so
%{awn_appletsdir}/switcher.desktop
%{_sysconfdir}/gconf/schemas/switcher.schemas

%dir %{awn_appletsdir}/trash
%{awn_appletsdir}/trash/trashapplet.glade
%attr(755,root,root) %{awn_appletsdir}/trash/trash.so
%{awn_appletsdir}/trash.desktop
%{_sysconfdir}/gconf/schemas/trash.schemas

%{awn_appletsdir}/volume-control
%{awn_appletsdir}/volume-control.desktop

%{awn_appletsdir}/weather
%{awn_appletsdir}/weather.desktop

%dir %{awn_appletsdir}/wobblyzini
%attr(755,root,root) %{awn_appletsdir}/wobblyzini/wobblyzini.so
%{awn_appletsdir}/wobblyzini.desktop
