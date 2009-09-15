%define module        bicyclerepair

Name:           python-%{module}
Version:        0.9
Release:        %mkrel 6
Epoch:          0
Summary:        Python Refactoring Browser
License:        BSD
Group:          System/Libraries
URL:            http://%{module}.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python-devel
Provides:       %{module} = %{epoch}:%{version}-%{release}
Requires:       python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

%description
The Python Refactoring Browser, helping Pythonistas everywhere
glide over the gory details of refactoring their code. Watch him
extract jumbled code into well ordered classes. Gasp, as he renames
all occurrences of a method. Thank You Bicycle Repair Man!

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES 

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL PKG-INFO NEWS README README.emacs README.vim
%{py_puresitedir}/*


