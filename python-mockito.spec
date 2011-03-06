#
# Conditional build:
%bcond_without	python2
%bcond_without	python3

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
%if %{with python2}
BuildRequires:	python-distribute
Requires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-2to3 >= 1:3.1.1-3
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mockito is a spying framework based on Java library with the same
name.

%package -n python3-%{module}
Summary:	Spying framework
Group:		Development/Languages/Python

%description -n python3-%{module}
Mockito is a spying framework based on Java library with the same
name.

%prep
%setup -q -n %{module}-python

find . -name '*.py' -type f | xargs %{__sed} -i -e '1s,^#!.*python,#!%{__python},'

%build
%if %{with python2}
%{__python} setup.py \
	build -b build-2

%endif

%if %{with python3}
%{__python3} setup.py \
	build -b build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%{__python} -- setup.py \
	build -b build-2 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# shutup check-files
%py_postclean
%endif

%if %{with python3}
%{__python3} -- setup.py \
	build -b build-3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# shutup check-files
%py3_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
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
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/mockito
%{py3_sitescriptdir}/mockito/*.py[co]
%dir %{py3_sitescriptdir}/mockito_test
%{py3_sitescriptdir}/mockito_test/*.py[co]
%dir %{py3_sitescriptdir}/mockito_util
%{py3_sitescriptdir}/mockito_util/*.py[co]
%{py3_sitescriptdir}/mockito-*.egg-info
%endif
