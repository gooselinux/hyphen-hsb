Name: hyphen-hsb
Summary: Upper Sorbian hyphenation rules
%define upstreamid 20080619
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source0: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/hyph-hsb.tex
Source1: http://www.tug.org/pipermail/tex-live/2005-June/008156.html
Group: Applications/Text
URL: http://tug.org/tex-hyphen
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel, elinks
Requires: hyphen
Patch0: hyphen-hsb-cleantex.patch

%description
Upper Sorbian hyphenation rules.

%prep
%setup -T -q -c -n hyphen-hsb
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-hsb.tex hyph_hsb_DE.dic UTF-8
echo "created with substring.pl by substrings.pl hyph-hsb.tex hyph_hsb_DE.dic UTF-8" > README
echo "---" >> README
echo "See 008156.html (http://www.tug.org/pipermail/tex-live/2005-June/008156.html) for COPYING details" >> README
echo "---" >> README
head -n 61 hyph-hsb.tex >> README

elinks -dump 008156.html -no-references > COPYING

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hsb_DE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080619-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080619-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080619-2
- links doesn't have a -no-references mode anymore

* Mon Mar 23 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080619-1
- initial version
