Name:           python-six
Version:        1.9.0
Release:        0
Summary:        Python 2 and 3 compatibility utilities
Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/six/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel

%description
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 2 build of the module.

%prep
%setup -q -n %{name}-%{version}

%build
cd six
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
cd six
rm -rf $RPM_BUILD_ROOT
python setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc six/README six/LICENSE
/%{python_sitearch}/*
