%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Java
Summary:	Inline::Java perl module
Summary(pl):	Modu³ perla Inline::Java
Name:		perl-Inline-Java
Version:	0.32
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
Requires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Java - Write Perl classes in Java.

%description -l pl
Modu³ Inline::Java - pozwalaj±cy na pisanie klas Perla w Javie.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO
%{perl_sitelib}/Inline/Java.pm
%{perl_sitelib}/Inline/Java
%{_mandir}/man3/*
