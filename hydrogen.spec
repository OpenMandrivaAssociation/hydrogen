%define	libname		%mklibname %{name}-core
%define	devname		%mklibname %{name}-core -d
%define	_appdatadir	%{_datadir}/appdata

%global	debug_package	%{nil}

%define	oname	Hydrogen

Summary:	An advanced Drum Machine
Name:	hydrogen
Version:	1.2.5
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://www.hydrogen-music.org
# Submodules are a pain
#Source0:	https://github.com/hydrogen-music/hydrogen/archive/%%{name}-%%{version}.tar.gz
Source0:	%{name}-%{version}.tar.xz
Patch0:	hydrogen-1.2.5-use-ladish-instead-of-lash.patch
BuildRequires:	appstream-util
BuildRequires:	cmake >= 3.8
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	git
BuildRequires:	ninja
BuildRequires:	qmake-qt6
BuildRequires:	alsa-oss-devel
BuildRequires:	ladspa-devel
BuildRequires:	libtar-devel
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblash)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(lrdf)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(portmidi)
BuildRequires:	pkgconfig(raptor)
# ATM rubberband2 support is experimental,
# but hydrogen can detect the binary and use it properly at runtime
#BuildRequires:	pkgconfig(rubberband)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(zlib)
Requires:	rubberband

%description
Hydrogen is an advanced drum machine for GNU/Linux. Its main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%files
%doc CHANGELOG.md README.md
%doc data/new_tutorial/*
%{_bindir}/%{name}
%{_bindir}/h2cli
%{_bindir}/h2player
%{_datadir}/applications/org.hydrogenmusic.%{oname}.desktop
%{_datadir}/metainfo/org.hydrogenmusic.%{oname}.metainfo.xml
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/??x??/apps/org.hydrogenmusic.%{oname}.png
%{_iconsdir}/hicolor/scalable/apps/org.hydrogenmusic.%{oname}.svg
%{_mandir}/man1/%{name}.1*

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for %{name}
Group:	System/Library

%description -n %{libname}
This package contains the library needed by %{name}.
%files -n %{libname}
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
%doc build/html/*
%{_includedir}/%{name}
%{_libdir}/libhydrogen-core.so

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake  \
	-DWANT_DEBUG=OFF \
	-DWANT_CPPUNIT=OFF \
	-DWANT_RUBBERBAND=OFF \
	-DWANT_QT6=ON \
	-DWANT_LASH=ON \
	-DWANT_LIBTAR=ON \
	-DWANT_LRDF=ON \
	-DWANT_PORTAUDIO=ON \
	-DWANT_PORTMIDI=ON \
	-G Ninja

%ninja_build

# Build also the devel docs, since we have a devel package
doxygen -u
doxygen Doxyfile


%install
%ninja_install -C build

# Provide a devel symlink to the main library
pushd %{buildroot}%{_libdir}
	ln -s libhydrogen-core-%{version}.so libhydrogen-core.so
popd

# Install more icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{64x64,48x48,32x32,24x24,16x16}/apps
cp data/img/gray/icon64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/org.hydrogenmusic.%{oname}.png
cp data/img/gray/icon48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/org.hydrogenmusic.%{oname}.png
cp data/img/gray/icon32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/org.hydrogenmusic.%{oname}.png
cp data/img/gray/icon24.png %{buildroot}%{_iconsdir}/hicolor/24x24/apps/org.hydrogenmusic.%{oname}.png
cp data/img/gray/icon16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/org.hydrogenmusic.%{oname}.png

# Remove useless directory: we take the tutorial with our macro
rm -rf %{buildroot}%{_datadir}/%{name}/doc

