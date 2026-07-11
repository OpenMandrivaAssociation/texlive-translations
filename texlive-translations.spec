%global tl_name translations
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.12
Release:	%{tl_revision}.1
Summary:	Internationalisation of LaTeX2e packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/translations
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translations.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translations.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package (once part of the exsheets package), provides a framework
for providing multilingual features to a LaTeX package. The package has
its own basic dictionaries for English, Brazilian, Catalan, Dutch,
French, German and Spanish; it aims to use translation material for
English, Dutch, French, German, Italian, Spanish, Catalan, Turkish,
Croatian, Hungarian, Danish and Portuguese from babel or polyglossia if
either is in use in the document. (Additional languages from the
multilingual packages may be possible: ask the author.)

