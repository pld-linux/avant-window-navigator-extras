#
# TODO:
# - check BRs ans Rs (I think they're too much as of now)
# - separate applets and plugins into subpackages
# - install and check plugins
# - make applets subpackage suggest all the applets
#
%define snap 20071024
Summary:	Extra applets and plugins for awn
Summary(pl.UTF-8):	Dodatkowe applety i wtyczki dla awn
Name:		avant-window-navigator-extras
Version:	0.2.%{snap}
Release:	0.1
License:	GPLv2
Group:		X11/Applications
#Source0:	http://avant-window-navigator.googlecode.com/files/%{name}-%{version}-2.tar.gz
Source0:	awn-extras-%{snap}.tar.bz2
# Source0-md5:	e27eba8b4aa03ff44c82f1975b1170a6
URL:		https://launchpad.net/awn-extras/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avant-window-navigator-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-doc-utils >= 0.7.1
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.35
BuildRequires:  libsexy-devel
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgtop-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
#Requires(post,preun):	GConf2 >= 2.14.0
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
%setup -q -n awn-extras-%{snap}

%build
# awn-applets core
cd awn-applets/awn-core-applets
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

# awn-applets core
%{__make} -C awn-applets/awn-core-applets install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

# awn-plugins

%clean
rm -rf $RPM_BUILD_ROOT

#%%post
#%%gconf_schema_install %{name}.schemas

#%%preun
#%%gconf_schema_uninstall switcher.schemas trash.schemas

%files -n avant-window-navigator-core-applets
%defattr(644,root,root,755)
#%{_sysconfdir}/gconf/schemas/*.schemas
%dir %{_datadir}/awn-core-applets

%dir %{awn_appletsdir}/awnnotificationdaemon
%attr(755,root,root) %{awn_appletsdir}/awnnotificationdaemon/awnnotificationdaemon.so
%{awn_appletsdir}/awnnotificationdaemon.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service

%dir %{awn_appletsdir}/awnsystemmonitor
%attr(755,root,root) %{awn_appletsdir}/awnsystemmonitor/awnsystemmonitor.so
%{awn_appletsdir}/awn-system-monitor.desktop

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

%dir %{awn_appletsdir}/trash
%{awn_appletsdir}/trash/trashapplet.glade
%attr(755,root,root) %{awn_appletsdir}/trash/trash.so
%{awn_appletsdir}/trash.desktop

%{awn_appletsdir}/volume-control
%{awn_appletsdir}/volume-control.desktop

%{awn_appletsdir}/weather
%{awn_appletsdir}/weather.desktop

%dir %{awn_appletsdir}/wobblyzini
%attr(755,root,root) %{awn_appletsdir}/wobblyzini/wobblyzini.so
%{awn_appletsdir}/wobblyzini.desktop
