%define upstream_name    Test-File
%define upstream_version 1.34

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.34
Release:	1

Summary:	Test file attributes
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-File-1.34.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Builder::Tester)
BuildArch:	noarch

%description
This modules provides a collection of test utilities for file
attributes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Wed Jul 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.0-1mdv2010.0
+ Revision: 393407
- update to 1.29
- fixed license tag

* Tue May 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.270.0-1mdv2010.0
+ Revision: 379877
- new version
- use new perl macro version
- drop failing test
- update to new version 1.26

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.25-2mdv2009.0
+ Revision: 268734
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2009.0
+ Revision: 218381
- update to new version 1.25
- update to new version 1.24
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2008.1
+ Revision: 104442
- update to new version 1.22


* Thu Jan 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2007.0
+ Revision: 110092
- new version

* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2007.1
+ Revision: 87846
- new version
- Import perl-Test-File

* Mon Jul 10 2006 Emmanuel Andry <eandry@mandriva.org> 1.16-1mdv2007.0
- New release 1.16

* Sat May 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdk
- New release 1.15

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.14-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Thu Mar 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.14-1mdk
- 1.14
- Remove patch 0

* Fri Mar 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.13-1mdk
- 1.13

* Thu Dec 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdk
- New release 1.12

* Wed Oct 05 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdk
- New release 1.11
- fix directory ownership
- spec cleanup

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.10-2mdk
- Fix BuildRequires
- mkrel

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10-1mdk
- initial Mandriva package


