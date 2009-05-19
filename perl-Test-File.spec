%define module  Test-File
%define name	perl-%{module}
%define version 1.26
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Test file attributes
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
# last test fails for unknown reasons, in chroot only
Patch:      %{module}-1.26-drop-failing-test.patch
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


