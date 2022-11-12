Name:		texlive-ednotes
Version:	35829
Release:	1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ednotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ednotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ednotes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A macro package for typesetting scholarly critical editions.
Provides macros for critical edition typesetting with LaTeX,
including support for line numbers and layers of footnotes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ednotes/edcntwd0.sty
%{_texmfdistdir}/tex/latex/ednotes/ednotes.sty
%{_texmfdistdir}/tex/latex/ednotes/lblchng1.sty
%{_texmfdistdir}/tex/latex/ednotes/mfparptc.sty
%{_texmfdistdir}/tex/latex/ednotes/mfparxsp.sty
%doc %{_texmfdistdir}/doc/latex/ednotes/CHANGES.txt
%doc %{_texmfdistdir}/doc/latex/ednotes/CHANGING.txt
%doc %{_texmfdistdir}/doc/latex/ednotes/README
%doc %{_texmfdistdir}/doc/latex/ednotes/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/ednotes/README4U.txt
%doc %{_texmfdistdir}/doc/latex/ednotes/READMORE.txt
%doc %{_texmfdistdir}/doc/latex/ednotes/ednotes.pdf
%doc %{_texmfdistdir}/doc/latex/ednotes/ednotes.tex
%doc %{_texmfdistdir}/doc/latex/ednotes/ednotugb.pdf
%doc %{_texmfdistdir}/doc/latex/ednotes/emathtst.tex
%doc %{_texmfdistdir}/doc/latex/ednotes/varnrule.tex
%doc %{_texmfdistdir}/doc/latex/ednotes/visible.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
