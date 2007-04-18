%define name    hydrogen
%define version 0.9.3
%define release %mkrel 1

%define	section	Multimedia/Sound
%define	title	Hydrogen
%define	Summary	Hydrogen Drum Machine

Summary:	%Summary
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPL
Group:		Sound
URL:		http://www.hydrogen-music.org
Source:		http://prdownloads.sourceforge.net/hydrogen/%{name}-%{version}.tar.bz2
#Patch0:		%{name}-0.9.2-songeditor.patch.bz2
BuildRoot:	%_tmppath/%{name}-buildroot
BuildRequires:	png-devel jpeg-devel libqt-devel pkgconfig
BuildRequires:	libalsa-devel jackit-devel libaudiofile-devel libsndfile-devel
BuildRequires:  libflac-devel

%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%prep
%setup -q
#%patch0 -p1 -b .songeditor

%build
QTDIR=%{_prefix}/lib/qt3
export QTDIR
%configure2_5x
%make

# fixed permissions
%__chmod 644 data/doc/tutorial_fr.docbook
%__chmod 644 data/doc/manual_fr.docbook

%install
%__rm -rf %buildroot
%makeinstall

#menu
%__mkdir_p %buildroot%_menudir
cat > %buildroot%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="x11" \
icon="%name.png" \
section="%section" \
title="%title" \
longtitle="%Summary"
EOF

#icons
%__mkdir_p %buildroot{%_miconsdir,%_iconsdir,%_liconsdir}
%__cp data/img/gray/icon48.png %buildroot%_liconsdir/%name.png
%__cp data/img/gray/icon32.png %buildroot%_iconsdir/%name.png
%__cp data/img/gray/icon16.png %buildroot%_miconsdir/%name.png

%post
%update_menus
		
%postun
%clean_menus

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/%name.desktop
%{_libdir}/%name
%{_menudir}/%name
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
