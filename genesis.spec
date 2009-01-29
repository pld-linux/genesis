# TODO
# - fix R
Summary:	Genesis Sync
Name:		genesis
Version:	0.4
Release:	0.1
License:	GPL v3
Group:		Applications/Networking
Source0:	http://launchpad.net/genesis-sync/new-config/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	ed74ce317468c75b11dbe939c02fc3cf
URL:		https://launchpad.net/genesis-sync
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python
#Requires:	python-configobj
Requires:	python-dbus
#Requires:	python-evolution or python-gnome2-desktop
#Requires:	python-gtk2
#Requires:	python-notify
#Requires:	python-xdg
Requires:	syncevolution
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genesis Sync is a GUI for the excellent SyncEvolution.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%find_lang genesis

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f genesis.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/genesis
%{_desktopdir}/genesis.desktop
%{_datadir}/genesis
%{_iconsdir}/hicolor/*/apps/genesis.*
%{_pixmapsdir}/genesis.png
%dir %{py_sitescriptdir}/Genesis
%{py_sitescriptdir}/Genesis/*.py[co]
