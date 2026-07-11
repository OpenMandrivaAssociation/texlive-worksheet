%global tl_name worksheet
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Easy creation of worksheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/worksheet
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/worksheet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/worksheet.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros and an environment for easy worksheet
creation: Use the exercise environment for formatting exercises in a
simple, efficient design; typeset customized and automatically numbered
worksheet titles in the same way as standard LaTeX titles (using
\maketitle); provide course and author information with a scrlayer-
scrpage based automated header; conforming to different babel languages.
(Currently English, French, and German are supported.)

