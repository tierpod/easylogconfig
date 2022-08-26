%global srcname easylogconfig

Name:           python-%{srcname}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Simple configuration for standart logging module

License:        MIT
URL:            https://github.com/tierpod/easylogconfig
Source0:        %pypi_source

BuildArch:      noarch

%description
Simple configuration for standart logging module

%package -n python3-%{srcname}
Summary:        Simple configuration for standart logging module
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Simple configuration for standart logging module

%prep
%autosetup -n %{srcname}-%{version}

%build
export LANG=en_US.utf-8
%py3_build

%install
export LANG=en_US.utf-8
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
