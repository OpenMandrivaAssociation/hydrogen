Summary:	Hydrogen Drum Machine
Name:		hydrogen
Version:	0.9.5.1
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://www.hydrogen-music.org
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		hydrogen-lrdf-pkg.patch
Patch1:		hydrogen-devel-warning.patch
BuildRequires:	scons
BuildRequires:	jpeg-devel
BuildRequires:	libtar-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lrdf)
BuildRequires:	pkgconfig(sndfile)

%description
Hydrogen is an advanced drum machine for GNU/Linux. Its main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%files
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_datadir}/pixmaps/h2-icon.svg

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
scons prefix="%{_prefix}"

%install
scons DESTDIR=%{buildroot} install

perl -pi -e 's,/usr/share/%{name}/data/img/gray/icon64.png,%{name},g' %{buildroot}%{_datadir}/applications/%{name}.desktop

#icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
cp data/img/gray/icon48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
cp data/img/gray/icon32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
cp data/img/gray/icon16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%changelog
* Fri Apr 08 2011 Frank Kober <emuse@mandriva.org> 0.9.5-1mdv2011.0
+ Revision: 651988
- new version 0.9.5

* Tue Jun 22 2010 Shlomi Fish <shlomif@mandriva.org> 0.9.4-0.rc1.1mdv2011.0
+ Revision: 548495
- Fix a typo - its

* Sun Jun 07 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.9.4-0.rc1.1mdv2010.0
+ Revision: 383447
- Fix file list
- Update BuildRequires
- Add Scons as BuildRequires
- Fix BuildRequires
- Update to 0.9.4  c1 ( Qt4 version)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 16 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.3-4mdv2008.1
+ Revision: 98751
- rebuild to fix FLAC errors causing no sound at all
- spec clean
- drop X-Mandriva menu category
- new license policy

* Thu Apr 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.3-3mdv2008.0
+ Revision: 14905
- bump release to differentiate from 2007.1 update package

* Thu Apr 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.3-2mdv2008.0
+ Revision: 14887
- don't package now non-existent menu entry
- remove old menu entry, emi is complaining
- XDG menu fixes
- revert previous incorrect fix for x86-64 build
- add patch2: correct fix for x86-64 build from upstream forum
- try to fix x86-64 build
- add patch0 (fix build with g++ 4.x)
- add patch1 (fix build with recent flac) (from arch)
- add libflac++ to BuildRequires
- rebuild with latest libflac
- install fd.o icons
- Import hydrogen



* Fri Feb 24 2006 Austin Acton <austin@mandriva.org> 0.9.3-1mdk
- New release 0.9.3
- disable patch (fixed I think...)
- fix source URL

* Wed Jan 25 2006 Tibor Pittich <Tibor.Pittich@mandriva.org> 0.9.2-4mdk
- add QTDIR variable

* Sat Nov 26 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 0.9.2-3mdk
- add patch0 which fixed song editor
- update url, improve description
- macroszification
- recreate menu section
- fixed bad permissions on fr docbook sources

* Wed Nov 09 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.2-2mdk
- Fix BuildRequires
- %%mkrel

* Mon Jul 25 2005 Austin Acton <austin@mandriva.org> 0.9.2-1mdk
- 0.9.2
- new source URL
- tidy buildrequires
- use included icons

* Wed May 25 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.1-2mdk
- Fix BuildRequires

* Sun Nov 28 2004 Austin Acton <austin@mandrake.org> 0.9.1-1mdk
- 0.9.1
- source URL

* Sat Sep 11 2004 Austin Acton <austin@mandrake.org> 0.9.0-1mdk
- 0.9.0
- drop libtoolize hack

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 0.8.2-1mdk
- 0.8.2

* Sat Dec 27 2003 Austin Acton <austin@linux.ca> 0.8.1-1mdk
- 0.8.1
- delib
- libtoolize

* Sun Aug 24 2003 Michael Scherer <scherer.michael@free.fr> 0.8.0-3mdk
- BuildRequires ( automake1.6 ) 

* Tue Jul 15 2003 Austin Acton <aacton@yorku.ca> 0.8.0-2mdk
- DIRM

* Sat May 24 2003 Austin Acton <aacton@yorku.ca> 0.8.0-1mdk
- 0.8.0

* Wed May 21 2003 Austin Acton <aacton@yorku.ca> 0.7.6-1mdk
- 0.7.6
- add manpage
- mklibname

* Mon Feb 24 2003 Austin Acton <aacton@yorku.ca> 0.7.5-1mdk
- 0.7.5

* Wed Feb 12 2003 Austin Acton <aacton@yorku.ca> 0.7.4-2mdk
- fix requires/provides

* Tue Feb 11 2003 Austin Acton <aacton@yorku.ca> 0.7.4-1mdk
- initial package
