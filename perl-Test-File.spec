%define module  Test-File
%define name	perl-%{module}
%define version 1.25
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Test file attributes
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
Buildrequires:	perl(Test::Builder::Tester)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This modules provides a collection of test utilities for file
attributes.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


