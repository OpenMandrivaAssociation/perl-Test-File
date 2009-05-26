%define module  Test-File
%define name	perl-%{module}
%define upstream_version 1.27
%define version     %perl_convert_version %{upstream_version}
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Test file attributes
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{upstream_version}.tar.gz
Buildrequires:	perl(Test::Builder::Tester)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This modules provides a collection of test utilities for file
attributes.

%prep
%setup -q -n %{module}-%{upstream_version} 

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


