#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Java
Summary:	Inline::Java - write Perl classes in Java
Summary(pl):	Inline::Java - pisanie klas Perla w Javie
Name:		perl-Inline-Java
Version:	0.43
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f671df7dd7480b4acc924f298193817d
BuildRequires:	jdk
%if %{with tests}
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl(Test) >= 1.13
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Java - Write Perl classes in Java.

%description -l pl
Modu³ Inline::Java - pozwalaj±cy na pisanie klas Perla w Javie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	J2SDK=/usr/lib/java \
	</dev/null

%{__make} java
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALLDIRS=vendor \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO
%{perl_vendorarch}/Inline/Java.pm
%{perl_vendorarch}/Inline/Java
%dir %{perl_vendorarch}/auto/Inline/Java
%dir %{perl_vendorarch}/auto/Inline/Java/JNI
%{perl_vendorarch}/auto/Inline/Java/JNI/JNI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Inline/Java/JNI/JNI.so
%{_mandir}/man3/*
