%define oname NetworkManager-fortisslvpn
%define name %(echo %{oname} | tr [:upper:] [:lower:])
%define url_ver %(echo %{version}|cut -d. -f1,2)

%define _disable_ld_no_undefined 1

%define pppd_version 2.4.5

Summary:	NetworkManager VPN integration for Fortinet SSLVPN
Name:		%{name}
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{url_ver}/NetworkManager-fortisslvpn-%{version}.tar.xz
# (upstream)
#Patch0:		https://gitlab.gnome.org/GNOME/NetworkManager-fortisslvpn/-/commit/66d431f18fd4812ed984790c877d965b35b69612.diff
#Patch1:		https://gitlab.gnome.org/GNOME/NetworkManager-fortisslvpn/-/commit/701f6f6f66f10e0b2ec6b0d6af80d1a8ec226a55.diff

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
%_pre_useradd nm-fortisslvpn %{_localstatedir}/lib/fortisslvpn /bin/false

