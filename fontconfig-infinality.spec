Summary:	Infinality font configuration file
Name:		fontconfig-infinality
Version:	3.1
Release:	4.R

License:	GPLv2
URL:		http://www.infinality.net/
Group:		System Environment/Libraries
Source0:	local.conf

Provides:	fonts-config = %{version}
Provides:	infinality-settings

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
* Thu Dec 19 2013 Arkady L. Shane <ashejn@russainfedora.ru> - 3.1-4.R
- drop obsolete depends

* Mon Apr 17 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 3.1-3.R
- drop infinality-settings.sh

* Mon Apr 17 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 3.1-2.R
- drop R: libXft-rfremix

* Thu Dec  1 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 3.1-1.R
- update to last infinality snapshot

* Fri Mar 18 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 3.0-4
- initial build for RFRemix

