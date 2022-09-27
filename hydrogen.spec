%define libname		%mklibname %{name}-core
%define devname		%mklibname %{name}-core -d
%define _appdatadir	%{_datadir}/appdata

%define debug_package	%{nil}

Name:           hydrogen
Version:        1.1.1
Release:        1
Summary:        An advanced Drum Machine
License:        GPLv2+
Group:          Sound
URL:            http://www.hydrogen-music.org
Source0:        https://github.com/hydrogen-music/hydrogen/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	ninja
BuildRequires:	desktop-file-utils
BuildRequires:	alsa-oss-devel
BuildRequires:	jpeg-devel
BuildRequires:	ladspa-devel
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	qmake5
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(lrdf)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	doxygen
BuildRequires:	appstream-util

Requires:	rubberband

%description
Hydrogen is an advanced drum machine for GNU/Linux. Its main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%files
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_iconsdir}/*/*/*/*
%{_appdatadir}/*.appdata.xml
%{_mandir}/man1/*.1*

#--------------------------------------------------------------------
%package -n %{libname}
Summary:	Library for %{name}
Group:		Sound

%description -n %{libname}
This package contains the library needed by %{name}.

%files -n %{libname}
%doc AUTHORS ChangeLog
%{_libdir}/libhydrogen-core-%{version}.so

#--------------------------------------------------------------------
%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the files needed for developing applications
which use %{name}.

%files -n %{devname}
%doc AUTHORS ChangeLog
%{_includedir}/%{name}

%prep
%autosetup -p1
%cmake_qt5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
