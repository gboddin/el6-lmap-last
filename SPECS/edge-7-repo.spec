Name:           edge-release
Version:        7 
Release:        2%{?dist} 
Summary:        Edge Packages for Enterprise Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

# This is a Edge maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            https://github.com/gboddin/el6-lamp-stack 
Source0:        https://repo.siwhine.net/EDGE-REPO-KEY.pub
Source1:        https://repo.siwhine.net/el/el7.repo

BuildArch:     noarch
Requires:      redhat-release >=  l
BuildRoot:      %{_tmppath}/%{name}-%{version}%{version}

%description
This package contains the Edge Packages for Enterprise Linux (Edge) repository
GPG key as well as configuration for yum.

%prep
%setup  -c -T

%build


%install
rm -rf %{buildroot} 

#GPG Key
install -Dpm 644 %{SOURCE0} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/EDGE-REPO-KEY

# yum
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1}  \
    %{buildroot}%{_sysconfdir}/yum.repos.d/edge.repo

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Wed Oct 19 2016 Gregory Boddin <gregory@siwhine.net> - 7-2
- Created package for easy install on RHELs

* Mon Aug 22 2016 Gregory Boddin <gregory@siwhine.net> - 7-1
- Created package for easy install on RHELs
 
* Mon Dec 16 2013 Dennis Gilmore <dennis@ausil.us> - 7-0.1
- initial epel 6 build. 

