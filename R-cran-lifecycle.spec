%define		fversion	%(echo %{version} |tr r -)
%define		modulename	lifecycle
%undefine	_debugsource_packages
Summary:	Manage the life cycle of your package functions
Name:		R-cran-%{modulename}
Version:	1.0.5
Release:	2
License:	MIT
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	bce35a7a89fe4108f262db3e441cccae
URL:		https://cran.r-project.org/package=%{modulename}
BuildRequires:	R
BuildRequires:	R-cran-cli
BuildRequires:	R-cran-glue
BuildRequires:	R-cran-rlang >= 1.1.0
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage the life cycle of your package functions.

%prep
%setup -q -c

%build
R CMD build --no-build-vignettes %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
