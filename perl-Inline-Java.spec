#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Java
Summary:	Inline::Java Perl module
Summary(cs):	Modul Inline::Java pro Perl
Summary(da):	Perlmodul Inline::Java
Summary(de):	Inline::Java Perl Modul
Summary(es):	Módulo de Perl Inline::Java
Summary(fr):	Module Perl Inline::Java
Summary(it):	Modulo di Perl Inline::Java
Summary(ja):	Inline::Java Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Java ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::Java
Summary(pl):	Modu³ Perla Inline::Java
Summary(pt):	Módulo de Perl Inline::Java
Summary(pt_BR):	Módulo Perl Inline::Java
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Java
Summary(sv):	Inline::Java Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Java
Summary(zh_CN):	Inline::Java Perl Ä£¿é
Name:		perl-Inline-Java
Version:	0.33
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c7da1744ffa5a56d0f8dfa586791899
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	rpm-perlprov >= 4.1-13
%{!?_without_tests:BuildRequires:	jdk}
BuildArch:	noarch
Requires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Java - Write Perl classes in Java.

%description -l pl
Modu³ Inline::Java - pozwalaj±cy na pisanie klas Perla w Javie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO
%{perl_vendorlib}/Inline/Java.pm
%{perl_vendorlib}/Inline/Java
%{_mandir}/man3/*
