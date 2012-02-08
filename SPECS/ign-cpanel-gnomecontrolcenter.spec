Summary:	IGOS Nusantara Control Panel module gnomecontrolcenter
Name:		ign-cpanel-gnomecontrolcenter
Version:	1.0.1
Release:	12.2.8
License:	GPLv2
Group:		System Environment/Base
URL:		http://igos-nusantara.or.id
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	ign-cpanel

%description
IGN CPANEL is a control panel for distribution for IGN GNU/Linux, which serves to manage
service, repository, packages, kernel modules, etc.. ign control panel made ​​with PHP-GTK2.

%prep
%setup -q -n %{name}-%{version}

%install
make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir 
/usr/share/ign-cpanel/modules/ign-cpanel-gnomecontrolcenter
%config %attr(0755,root,root) /usr/share/ign-cpanel/modules/ign-cpanel-gnomecontrolcenter/*

%changelog
* Wed Feb 8 2012 Ibnu Yahya <ibnu.yahya@toroo.org>
- build module
