%define module        bicyclerepair

Name:           python-%{module}
Version:        0.9
Release:        7
Epoch:          0
Summary:        Python Refactoring Browser
License:        BSD
Group:          System/Libraries
URL:            https://%{module}.sourceforge.net/
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




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:0.9-6mdv2010.0
+ Revision: 442040
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0:0.9-5mdv2009.1
+ Revision: 323537
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:0.9-4mdv2009.0
+ Revision: 259499
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:0.9-3mdv2009.0
+ Revision: 247386
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0:0.9-1mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 12 2007 David Walluck <walluck@mandriva.org> 0:0.9-1mdv2007.1
+ Revision: 141496
- Import python-bicyclerepair

* Sun Mar 11 2007 David Walluck <walluck@mandriva.org> 0:0.9-1mdv2007.1
- release

