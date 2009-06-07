%define name    hydrogen
%define version 0.9.4
%define release %mkrel 0.rc1.1

%define	section	Multimedia/Sound
%define	title	Hydrogen
%define	Summary	Hydrogen Drum Machine

Summary:	%Summary
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPLv2+
Group:		Sound
URL:		http://www.hydrogen-music.org
Source:		http://prdownloads.sourceforge.net/%name/%name-%version-rc1-1.tar.gz
Patch0:		%{name}-0.9.3-g++4.patch
Patch1:		%{name}-0.9.3-build-flac.patch
Patch2:		%{name}-0.9.3-lib64.patch
BuildRoot:	%_tmppath/%{name}-buildroot
BuildRequires:	png-devel 
BuildRequires:  jpeg-devel 
BuildRequires:  qt4-devel 
BuildRequires:  pkgconfig
BuildRequires:	libalsa-devel 
BuildRequires:  jackit-devel 
BuildRequires:  libaudiofile-devel 
BuildRequires:  libsndfile-devel
BuildRequires:  libflac-devel 
BuildRequires:  libflac++-devel
BuildRequires:	desktop-file-utils
BuildRequires:  liblrdf-devel
BuildRequires:  scons
BuildRequires:  libtar-devel

%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/applications/%name.desktop
%{_datadir}/%name
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_datadir}/pixmaps/h2-icon.svg

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-rc1-1
#%patch0 -p0 -b .g++4
#%patch1 -p0 -b .buildflac
#%patch2 -p0 -b .lib64

%build
scons prefix="%_prefix"

# fixed permissions
#%__chmod 644 data/doc/tutorial_fr.docbook
#%__chmod 644 data/doc/manual_fr.docbook

%install
%__rm -rf %buildroot
scons DESTDIR=%buildroot install

perl -pi -e 's,/usr/share/%{name}/data/img/gray/icon64.png,%{name},g' %buildroot%{_datadir}/applications/%{name}.desktop

#icons
%__mkdir_p %buildroot%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
%__cp data/img/gray/icon48.png %buildroot%_iconsdir/hicolor/48x48/apps/%{name}.png
%__cp data/img/gray/icon32.png %buildroot%_iconsdir/hicolor/32x32/apps/%{name}.png
%__cp data/img/gray/icon16.png %buildroot%_iconsdir/hicolor/16x16/apps/%{name}.png

%clean
%__rm -rf %buildroot
