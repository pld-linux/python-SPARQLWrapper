#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	SPARQL Endpoint interface to Python 2
Summary(pl.UTF-8):	Interfejs SPARQL Endpoint do Pythona 2
Name:		python-SPARQLWrapper
Version:	1.8.4
Release:	1
License:	W3C
Group:		Libraries/Python
#Source0Download: https://github.com/RDFLib/sparqlwrapper/releases
Source0:	https://github.com/RDFLib/sparqlwrapper/archive/%{version}/sparqlwrapper-%{version}.tar.gz
# Source0-md5:	177c10d032de0f37feb5108120c2bb5a
URL:		https://rdflib.github.io/sparqlwrapper/
%{?with_doc:BuildRequires:	epydoc}
BuildRequires:	rpm-pythonprov
# for the py_build, py_install macros
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-isodate
BuildRequires:	python-keepalive >= 0.5
BuildRequires:	python-rdflib >= 4.2.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-isodate
BuildRequires:	python3-keepalive >= 0.5
BuildRequires:	python3-rdflib >= 4.2.2
%endif
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%description -l pl.UTF-8
Ten moduł to obudowanie usługi SPARQL, pomagające przy tworzeniu
URI zapytania oraz ewentualnie konwertujące wynik do bardziej
zarządzalnego formatu.

%package -n python3-SPARQLWrapper
Summary:	SPARQL Endpoint interface to Python 3
Summary(pl.UTF-8):	Interfejs SPARQL Endpoint do Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-SPARQLWrapper
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%description -n python3-SPARQLWrapper -l pl.UTF-8
Ten moduł to obudowanie usługi SPARQL, pomagające przy tworzeniu
URI zapytania oraz ewentualnie konwertujące wynik do bardziej
zarządzalnego formatu.

%package apidocs
Summary:	API documentation for SPARQLWrapper module
Summary(pl.UTF-8):	Dokumentacja API modułu SPARQLWrapper
Group:		Documentation

%description apidocs
API documentation for SPARQLWrapper module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu SPARQLWrapper.

%prep
%setup -q -n sparqlwrapper-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} doc
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.md ChangeLog.txt LICENSE.txt MANAGEMENT.md README.md
%{py_sitescriptdir}/SPARQLWrapper
%{py_sitescriptdir}/SPARQLWrapper-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-SPARQLWrapper
%defattr(644,root,root,755)
%doc AUTHORS.md ChangeLog.txt LICENSE.txt MANAGEMENT.md README.md
%{py3_sitescriptdir}/SPARQLWrapper
%{py3_sitescriptdir}/SPARQLWrapper-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/*
%endif
