Name:		texlive-worksheet
Version:	48423
Release:	2
Summary:	Easy creation of worksheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/worksheet
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/worksheet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/worksheet.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros and an environment for easy
worksheet creation: Use the exercise environment for formating
exercises in a simple, efficient design; typeset customized and
automatically numbered worksheet titles in the same way as
standard LaTeX titles (using \maketitle); provide course and
author information with a scrlayer-scrpage based automated
header; conforming to different babel languages. (Currently
English, French, and German are supported.)

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/worksheet
%doc %{_texmfdistdir}/doc/latex/worksheet

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
