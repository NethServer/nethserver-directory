Name: nethserver-directory
Summary: LDAP backend for user and group accounts
Version: 2.3.0
Release: 2%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 

Requires: coreutils
Requires: pam_ldap >= 185-5, nss-pam-ldapd >= 0.7.5-3, libuser >= 0.56.13-5
Requires: openldap, openldap-clients, openldap-servers
Requires: perl-LDAP
Requires: perl-Crypt-Cracklib
Requires: nethserver-base
# send expiring password warnings: 
Requires: mailx, postfix, anacron
Obsoletes: nethserver-password
Provides: nethserver-password

BuildRequires: perl
BuildRequires: nethserver-devtools
BuildRequires: gettext

%description
LDAP backend for user and group accounts

%prep
%setup -q

%build

mkdir -p root%{perl_vendorlib}
mv -v NethServer root%{perl_vendorlib}
mv -v esmith root%{perl_vendorlib}

perl createlinks
%{makedocs}

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist


%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%doc scripts/fix_accounts
%doc scripts/import_users
%doc scripts/fix_migration_home

%changelog
* Tue Nov 08 2016 Davide Principi <davide.principi@nethesis.it> - 2.3.0-2
- Fix security issue - Bug Nethesis/dev#5029

* Thu Sep 24 2015 Davide Principi <davide.principi@nethesis.it> - 2.3.0-1
- Obsolete nethserver-password by merging it into nethserver-directory - Enhancement #3260 [NethServer]

* Mon Sep 14 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.2.3-1
- Avoid slapd restart when updating openldap-servers package - Enhancement #3253 [NethServer]

* Wed May 20 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.2.2-1
- Localize "password expire" notifications - Enhancement #2887 [NethServer]

* Tue May 19 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.2.1-1
- Create User tab not reset - Bug #2728 [NethServer]

* Thu Apr 23 2015 Davide Principi <davide.principi@nethesis.it> - 2.2.0-1
- Language packs support - Feature #3115 [NethServer]
- Expired password visual notification - Feature #2980 [NethServer]

* Tue Mar 03 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.1.0-1
- Differentiate root and admin users - Feature #3026 [NethServer]

* Thu Jan 29 2015 Davide Principi <davide.principi@nethesis.it> - 2.0.6-1.ns6
- Password renewal link doesn't use httpd-admin TCPPort  - Bug #2993 [NethServer]

* Tue Dec 09 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.5-1.ns6
- Modify all users if the ldap organisation contacts is updated - Bug #2931 [NethServer]
- Drop TCP wrappers hosts.allow hosts.deny templates - Enhancement #2785 [NethServer]

* Mon Nov 03 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.4-1.ns6
- slapd Upstart status is out of control if BDB is corrupted - Bug #2928
- Drop TCP wrappers hosts.allow hosts.deny templates - Enhancement #2785

* Thu Jun 19 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.3-1.ns6
- Flexible "what" clause in enforceAccessDirective() - Enhancement #2757
- Missing Italian translation - Bug #2706
- Import users from a file - Feature #2666

* Mon Mar 10 2014 Davide Principi <davide.principi@nethesis.it> - 2.0.2-1.ns6
- Backup config: can't restore LDAP dump - Bug #2680 [NethServer]

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 2.0.1-1.ns6
- Revamp web UI style - Enhancement #2656 [NethServer]
- Skip deleted accounts in dashboard - Bug #2648 [NethServer]
- Implement hostname-modify event for samba  - Enhancement #2626 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 2.0.0-1.ns6
- Move admin user in LDAP DB - Feature #2492 [NethServer]
- IPSec: honor VPNClientAccess property - Enhancement #2294 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]
- Dashboard: new widgets - Enhancement #1671 [NethServer]
- Users and groups migration script - Enhancement #1655 [NethServer]

* Wed Dec 18 2013 Davide Principi <davide.principi@nethesis.it> - 1.3.0-1.ns6
- Password expiration warnings are sent to locked users - Bug #2250 [NethServer]
- Directory: backup service accounts passwords  - Enhancement #2063 [NethServer]
- Service supervision with Upstart - Feature #2014 [NethServer]

* Wed Oct 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.3-1.ns6
- Add AdminIsNotRoot property #2277
- Add language code to URLs  #2113
- warnpassexpire script: conform to user state machine - #1073
- Db defaults: remove Runlevels prop. Refs #206

* Fri Jul 12 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1.ns6
- Backup: implement and document full restore #2043
- nethserver-directory: fix nsstest user creation #1981

* Wed May 29 2013 Davide Principi <davide.principi@nethesis.it> - 1.2.1-1.ns6
- Create nsstest user and group in LDAP. Bugfix #1981

* Tue Apr 30 2013 Davide Principi <davide.principi@nethesis.it> - 1.2.0-1.ns6
- Full automatic package install/upgrade/uninstall support #1870
- Default user Organization Contact props #1853
- Fixed samba password hash disclosure: slapd ACLs applied on both BDB and rwm frontends #1894
- hostname-modify event support #1010
- Change default slapd log level to 0  #1835
- /etc/pam.d/system-auth-nh, /etc/nsswitch.conf: use new template format #1746

* Tue Mar 19 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1.ns6
- Add migration code

* Mon Feb 11 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1.ns6
- Disable default group home directory cretion. 
  Refs #1638

* Thu Jan 31 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1.ns6
- NethServer/Directory.pm: added configServiceAccount() method. 
  Refs #1639 -- LDAP service accounts
- Configure default certificate management. 
  Refs #1632


