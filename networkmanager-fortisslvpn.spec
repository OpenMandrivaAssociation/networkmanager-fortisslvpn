%define oname NetworkManager-fortisslvpn
%define name %(echo %{oname} | tr [:upper:] [:lower:])
%define url_ver %(echo %{version}|cut -d. -f1,2)

%define _disable_ld_no_undefined 1

%define pppd_version 2.4.5

Summary:	NetworkManager VPN integration for Fortinet SSLVPN
Name:		%{name}
Version:	1.4.0
Release:	2
License:	GPLv2+
Group:		System/Base
Url:		https://gitlab.gnome.org/GNOME/NetworkManager-fortisslvpn
Source0:	https://download.gnome.org/sources/NetworkManager-fortisslvpn/1.4/NetworkManager-fortisslvpn-%{version}.tar.xz

BuildRequires:  ppp-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(libnma)

Requires:	dbus
Requires:	gtk+3
Requires:	gtk4
Requires:	NetworkManager
Requires:	openfortivpn

%description
This package contains software for integrating the Fortinet SSLVPN
with NetworkManager and the GNOME desktop.

%files -f NetworkManager-fortisslvpn.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_sysconfdir}/dbus-1/system.d/nm-fortisslvpn-service.conf
%{_libdir}/pppd/%{pppd_version}/nm-fortisslvpn-pppd-plugin.so
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn-editor.so
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-fortisslvpn-editor.so
%{_libexecdir}/nm-fortisslvpn-auth-dialog
%{_libexecdir}/nm-fortisslvpn-pinentry
%{_libexecdir}/nm-fortisslvpn-service
%{_prefix}/lib/NetworkManager/VPN/nm-fortisslvpn-service.name
%{_sharedstatedir}/%{oname}
%{_datadir}/appdata/network-manager-fortisslvpn.metainfo.xml

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%configure \
	--disable-static \
	--enable-more-warnings \
	--without-libnm-glib \
	--with-gtk4

%make_build

%install
%make_install

# locales
%find_lang %{oname}

%pre
getent group nm-fortisslvpn >/dev/null || groupadd -r nm-fortisslvpn
getent passwd nm-fortisslvpn >/dev/null || \
        useradd -r -g nm-fortisslvpn -d / -s /sbin/nologin \
        -c "Default user for running openfortivpn spawned by NetworkManager" nm-fortisslvpn
exit 0
