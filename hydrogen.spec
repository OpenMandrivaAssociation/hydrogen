%define major		0.9.6.1
%define libname		%mklibname %{name}-core %{major}
%define devname		%mklibname %{name}-core -d
%define _appdatadir	%{_datadir}/appdata

%define debug_package	%{nil}

Name:           hydrogen
Version:        0.9.6.1
Release:        2
Summary:        An advanced Drum Machine
License:        GPLv2+
Group:          Sound
URL:            http://www.hydrogen-music.org
Source0:        https://github.com/%{name}-music/%{name}/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	desktop-file-utils
BuildRequires:	alsa-oss-devel
BuildRequires:	jpeg-devel
BuildRequires:	ladspa-devel
BuildRequires:	qt4-devel
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
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hydrogen.png
%{_appdatadir}/*.appdata.xml

#--------------------------------------------------------------------
%package -n %{libname}
Summary:	Library for %{name}
Group:		Sound

%description -n %{libname}
This package contains the library needed by %{name}.

%files -n %{libname}
%doc AUTHORS ChangeLog
%{_libdir}/libhydrogen-core-%{major}.so

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
%{_libdir}/libhydrogen-core.so

%prep
%setup -q

%build
export PATH=/usr/lib/qt4/bin:$PATH
%cmake
%make

%install
%makeinstall_std -C build
pushd %{buildroot}%{_libdir}
ln -s libhydrogen-core-%{major}.so libhydrogen-core.so
popd

#icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
cp data/img/gray/icon48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
cp data/img/gray/icon32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
cp data/img/gray/icon16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
cp %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png %{buildroot}%{_iconsdir}/


desktop-file-install \
		--remove-category Application \
		--remove-category Sound \
		--remove-key Encoding \
		--remove-key=FilePattern \
		--set-icon=%{name} \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop
		
# appdata
mkdir -p %{buildroot}%{_appdatadir}		
appstream-util appdata-from-desktop %{buildroot}%{_datadir}/applications/hydrogen.desktop hydrogen.appdata.xml
cp hydrogen.appdata.xml %{buildroot}%{_appdatadir}/






