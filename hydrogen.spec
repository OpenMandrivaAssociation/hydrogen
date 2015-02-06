Summary:	Hydrogen Drum Machine
Name:		hydrogen
Version:	0.9.5.1
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://www.hydrogen-music.org
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		hydrogen-lrdf-pkg.patch
Patch1:		hydrogen-devel-warning.patch
Patch2:		hydrogen-0.9.5.1-sfmt.patch
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

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Workaround due to change in scons behavior. Just a temporary fix since upstream
# switched to cmake in trunk
sed -i -e '/path.walk/d' -e 's|\(pkg_ver.rstrip.*\)|\1[0:3]|' Sconstruct

%build
%scons prefix="%{_prefix}" optflags="%{optflags}"

%install
scons DESTDIR=%{buildroot} install

perl -pi -e 's,/usr/share/%{name}/data/img/gray/icon64.png,%{name},g' %{buildroot}%{_datadir}/applications/%{name}.desktop

#icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
cp data/img/gray/icon48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
cp data/img/gray/icon32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
cp data/img/gray/icon16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

