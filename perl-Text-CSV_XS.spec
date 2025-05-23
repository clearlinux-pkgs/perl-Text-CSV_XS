#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Text-CSV_XS
Version  : 1.60
Release  : 80
URL      : https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-1.60.tgz
Source0  : https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-1.60.tgz
Summary  : Comma-Separated Values manipulation routines
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Text-CSV_XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Module:
Text::CSV_XS
Description:
Text::CSV_XS provides facilities for the composition and decomposition
of comma-separated values.   An instance of the Text::CSV_XS class can
combine fields into a CSV string and parse a CSV string into fields.

%package dev
Summary: dev components for the perl-Text-CSV_XS package.
Group: Development
Provides: perl-Text-CSV_XS-devel = %{version}-%{release}
Requires: perl-Text-CSV_XS = %{version}-%{release}

%description dev
dev components for the perl-Text-CSV_XS package.


%package perl
Summary: perl components for the perl-Text-CSV_XS package.
Group: Default
Requires: perl-Text-CSV_XS = %{version}-%{release}

%description perl
perl components for the perl-Text-CSV_XS package.


%prep
%setup -q -n Text-CSV_XS-1.60
cd %{_builddir}/Text-CSV_XS-1.60
pushd ..
cp -a Text-CSV_XS-1.60 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::CSV_XS.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
