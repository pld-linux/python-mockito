#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	mockito
Summary:	Spying framework
Name:		python-%{module}
Version:	0.5.1
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://mockito-python.googlecode.com/files/%{module}-python-%{version}.tar.gz
# Source0-md5:	814669d5a6f1dc051f409d8c3521da64
URL:		http://code.google.com/p/mockito-python
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mockito is a spying framework based on Java library with the same
name.

%prep
%setup -q -n %{module}-python

find . -name '*.py' -type f | xargs %{__sed} -i -e '1s,^#!.*python,#!%{__python},'

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/mockito
%{py_sitescriptdir}/mockito/*.py[co]
%dir %{py_sitescriptdir}/mockito_test
%{py_sitescriptdir}/mockito_test/*.py[co]
%dir %{py_sitescriptdir}/mockito_util
%{py_sitescriptdir}/mockito_util/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/mockito-*.egg-info
%endif
