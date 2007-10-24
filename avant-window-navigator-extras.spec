#
# TODO:
# - check BRs ans Rs (I think they're too much as of now)
# - separate applets and plugins into subpackages
# - install and check plugins
# - make applets subpackage suggest all the applets
#
%define snap 20071024
%define _basename avant-window-navigator
%define _realname awn-extras
Summary:	Extra applets and plugins for awn
Summary(pl.UTF-8):Dodatkowe applety i wtyczki dla awn
Name:		%{_basename}-extras
Version:	0.2.%{snap}
Release:	0.1
License:	GPLv2
Group:		X11/Applications
#Source0:	http://avant-window-navigator.googlecode.com/files/%{name}-%{version}-2.tar.gz
Source0:	%{_realname}-%{snap}.tar.bz2
# Source0-md5:	e27eba8b4aa03ff44c82f1975b1170a6
URL:		https://launchpad.net/awn-extras/
BuildRequires:	%{_basename}-devel
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
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
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires(post,preun):	GConf2 >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define     _appletsdir     %{_libdir}/awn/applets
%description
Generic package for all core awn-plugins.

%description -l pl.UTF-8
Paczka wspólna dla wszystkich głównym wtyczek dla awn.

%package -n %{_basename}-core-applets
Summary:	Core applets for awn
Summary(pl.UTF-8):Kluczowe applety dla awn
Group:		X11/Applications
Requires:	%{_basename} = %{version}

%description -n %{_basename}-core-applets
Core applets for awn.

%description -n %{_basename}-core-applets -l pl.UTF-8
Kluczowe applety dla awn.

%package -n %{_basename}-plugins
Summary:	Pluggins for awn
Summary(pl.UTF-8):Wtyczki dla awn
Group:		X11/Applications
Requires:	%{_basename} = %{version}-%{release}

%description -n %{_basename}-plugins
Pluggins for awn.

%description -n %{_basename}-plugins -l pl.UTF-8
Wtyczki dla awn.

%prep
%setup -q -n %{_realname}-%{snap}

%build

###
# awn-applets core
###
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

###
# awn-applets core
###
cd awn-applets/awn-core-applets
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

###
# awn-plugins
###

%clean
rm -rf $RPM_BUILD_ROOT

#%%post
#%%gconf_schema_install %{name}.schemas
#/sbin/ldconfig

#%%preun
#%%gconf_schema_uninstall switcher.schemas trash.schemas

#%%postun
#/sbin/ldconfig

%files -n %{_basename}-core-applets
%defattr(644,root,root,755)
#%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service
%dir %{_appletsdir}/awnnotificationdaemon
%{_appletsdir}/awnnotificationdaemon/awnnotificationdaemon.so
%{_appletsdir}/awnnotificationdaemon.desktop
%dir %{_appletsdir}/awnsystemmonitor
%{_appletsdir}/awnsystemmonitor/awnsystemmonitor.so
%{_appletsdir}/awn-system-monitor.desktop
%{_appletsdir}/battery-applet
%{_appletsdir}/battery-applet.desktop
%dir %{_appletsdir}/mainmenu
%{_appletsdir}/BlingSwitcher
%{_appletsdir}/PySwitcher.desktop
%dir %{_appletsdir}/clock
%{_appletsdir}/clock/clock.so
%{_appletsdir}/clock.desktop
%dir %{_appletsdir}/filebrowser
%{_appletsdir}/filebrowser/filebrowser.so
%{_appletsdir}/filebrowser.desktop
%{_datadir}/awn-core-applets/filebrowser.svg
%{_appletsdir}/gmail
%{_appletsdir}/awngmail.desktop
%dir %{_appletsdir}/mainmenu
%{_appletsdir}/mainmenu/mainmenu.so
%{_appletsdir}/main-menu.desktop
%{_appletsdir}/media-control
%{_appletsdir}/media-control.desktop
%{_appletsdir}/media-icon-*
%{_appletsdir}/medialogo*.desktop
%dir %{_appletsdir}/notification-area
%{_appletsdir}/notification-area/notification-area.so
%{_appletsdir}/notification-area.desktop
%{_appletsdir}/quit-applet
%{_appletsdir}/quit-applet.desktop
%{_datadir}/awn-core-applets/notification.svg
%dir %{_appletsdir}/separator
%{_appletsdir}/separator/separator.so
%{_appletsdir}/separator.desktop
%{_datadir}/awn-core-applets/separator.svg
%{_appletsdir}/showdesktop
%{_appletsdir}/showdesktop.desktop
%{_appletsdir}/stacks
%{_appletsdir}/stacks.desktop
%dir %{_appletsdir}/switcher
%{_appletsdir}/switcher/switcher.so
%{_appletsdir}/switcher.desktop
%dir %{_appletsdir}/trash
%{_appletsdir}/trash/trashapplet.glade
%{_appletsdir}/trash/trash.so
%{_appletsdir}/trash.desktop
%{_appletsdir}/volume-control
%{_appletsdir}/volume-control.desktop
%{_appletsdir}/weather
%{_appletsdir}/weather.desktop
%dir %{_appletsdir}/wobblyzini
%{_appletsdir}/wobblyzini/wobblyzini.so
%{_appletsdir}/wobblyzini.desktop
