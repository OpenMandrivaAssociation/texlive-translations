Name:		texlive-translations
Version:	61896
Release:	2
Summary:	Internationalisation of LaTeX2e packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/translations
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translations.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translations.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/translations
%doc %{_texmfdistdir}/doc/latex/translations

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
