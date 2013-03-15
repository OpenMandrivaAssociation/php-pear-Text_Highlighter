%define		_class		Text
%define		_subclass	Highlighter
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.7.1
Release:	8
Summary:	Syntax highlighting
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Text_Highlighter/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Text_Highlighter is a package for syntax highlighting.

It provides a base class providing all the functionality, and a
descendent classes geneator class.

The main idea is to simplify creation of subclasses implementing
syntax highlighting for particular language. Subclasses do not
implement any new functionality, they just provide syntax
highlighting rules. The rules sources are in XML format.

To create a highlighter for a language, there is no need to code a new
class manually. Simply describe the rules in XML file and use
Text_Highlighter_Generator to create a new class.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data/TODO

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/README
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-6mdv2011.0
+ Revision: 667642
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-5mdv2011.0
+ Revision: 607151
- rebuild

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-4mdv2010.1
+ Revision: 466323
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.7.1-3mdv2010.0
+ Revision: 426669
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-2mdv2009.1
+ Revision: 321903
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdv2009.0
+ Revision: 272598
- 0.7.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-3mdv2009.0
+ Revision: 224883
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-2mdv2008.1
+ Revision: 178539
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-1mdv2008.0
+ Revision: 54559
- 0.7.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-1mdv2007.0
+ Revision: 81226
- Import php-pear-Text_Highlighter

* Sat Apr 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-1mdk
- 0.6.9

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.8-1mdk
- 0.6.8
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-1mdk
- 0.6.6

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-1mdk
- initial Mandriva package (PLD import)

