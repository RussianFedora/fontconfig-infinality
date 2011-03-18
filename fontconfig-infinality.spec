Summary:	Infinality font configuration file
Name:		fontconfig-infinality
Version:	3.0
Release:	4

License:	GPLv2
URL:		http://www.infinality.net/
Group:		System Environment/Libraries
Source0:	local.conf

Requires:	libXft-rfremix
Requires:	cairo-freeworld
Requires:	freetype-infinality

Provides:	fonts-config = %{version}

BuildArch:	noarch


%description
A /etc/fonts/local.conf file that is configured to render fonts the way
Infinality likes them, when using patches from http://www.infinality.net

%prep


%build


%install
install -dD %{buildroot}/etc/fonts/
cp %{SOURCE0} %{buildroot}%{_sysconfdir}/fonts/local.conf


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/fonts/local.conf


%changelog
* Fri Mar 18 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 3.0-4
- initial build for RFRemix

