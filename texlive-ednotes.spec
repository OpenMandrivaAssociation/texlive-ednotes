# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/ednotes
# catalog-date 2008-01-07 00:37:03 +0100
# catalog-license lppl
# catalog-version 1.3a
Name:		texlive-ednotes
Version:	1.3a
Release:	1
Summary:	Typeset scholarly editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ednotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ednotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ednotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A macro package for typesetting scholarly critical editions.
Provides macros for critical edition typesetting with LaTeX,
including support for line numbers and layers of footnotes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
