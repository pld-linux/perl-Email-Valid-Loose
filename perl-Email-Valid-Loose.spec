#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Valid-Loose
Summary:	Email::Valid::Loose - Email::Valid which allows dot before @ mark
Summary(pl):	Email::Valid::Loose - Email::Valid zezwalaj±cy na kropkê przed znakiem @
Name:		perl-Email-Valid-Loose
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a9893651ffb6af6d37f42caa0f49e03
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Valid
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Valid::Loose is a subclass of Email::Valid, which allows .
(dot) before @ (at-mark). It is invalid in RFC822, but is commonly
used in some of mobile phone addresses in Japan (like docomo.ne.jp or
jp-t.ne.jp).

%description -l pl
Email::Valid::Loose to podklasa Email::Valid zezwalaj±ca na . (kropkê)
przed @ (znakiem "at"). Jest to niepoprawne wg RFC822, ale powszechnie
u¿ywane w niektórych adresach telefonów komórkowych w Japonii (na
przyk³ad docomo.ne.jp lub jp-t.ne.jp).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Email/Valid
%{perl_vendorlib}/Email/Valid/*.pm
%{_mandir}/man3/*
