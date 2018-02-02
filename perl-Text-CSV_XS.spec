#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-CSV_XS
Version  : 1.34
Release  : 25
URL      : https://www.cpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-1.34.tgz
Source0  : https://www.cpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-1.34.tgz
Summary  : Comma-Separated Values manipulation routines
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Text-CSV_XS-lib
Requires: perl-Text-CSV_XS-doc

%description
Module:
Text::CSV_XS
Description:
Text::CSV_XS provides facilities for the composition and decomposition
of comma-separated values.  An instance of the Text::CSV_XS class can
combine fields into a CSV string and parse a CSV string into fields.

%package doc
Summary: doc components for the perl-Text-CSV_XS package.
Group: Documentation

%description doc
doc components for the perl-Text-CSV_XS package.


%package lib
Summary: lib components for the perl-Text-CSV_XS package.
Group: Libraries

%description lib
lib components for the perl-Text-CSV_XS package.


%prep
%setup -q -n Text-CSV_XS-1.34

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Text/CSV_XS.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Text/CSV_XS/CSV_XS.so
