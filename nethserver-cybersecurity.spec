Name: nethserver-cybersecurity
Version: 0.0.0
Release: 1%{?dist}
Summary: Cybersecurity is an application of security

License: GPLv3
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
# Execute prep-sources to create Source1
Source1: %{name}.tar.gz
BuildArch:	noarch

BuildRequires: nethserver-devtools
Requires:	nethserver-cockpit

%description
Cybersecurity is an application that bundles security tools and network analysis.

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/

tar xvf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
chmod +x %{buildroot}/usr/libexec/nethserver/api/%{name}/*

%{genfilelist} %{buildroot} > filelist
%files -f filelist

#%dir %{_nseventsdir}/%{name}-update

%changelog
