# revision 31800
# category Package
# catalog-ctan /macros/latex/contrib/translations
# catalog-date 2013-09-30 07:01:40 +0200
# catalog-license lppl1.3
# catalog-version 1.1a
Name:		texlive-translations
Version:	1.1a
Release:	4
Summary:	Internationalisation of LaTeX2e packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/translations
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translations.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translations.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package (once part of the exsheets package), provides a
framework for providing multilingual features to a LaTeX
package. The package has its own basic dictionaries for
English, French, German and Spanish; it aims to use translation
material for English, French, German, Italian, Spanish,
Catalan, Turkish, Croatian, Hungarian, Danish and Portuguese
from babel or polyglossia if either is in use in the document.
(Additional languages from the multilingual packages may be
possible: ask the author.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-english.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-french.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-german.trsl
%{_texmfdistdir}/tex/latex/translations/translations-basic-dictionary-spanish.trsl
%{_texmfdistdir}/tex/latex/translations/translations.sty
%doc %{_texmfdistdir}/doc/latex/translations/README
%doc %{_texmfdistdir}/doc/latex/translations/translations_en.pdf
%doc %{_texmfdistdir}/doc/latex/translations/translations_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
