%define name    hydrogen
%define version 0.9.3
%define release %mkrel 6

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
Source:		http://prdownloads.sourceforge.net/hydrogen/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.9.3-g++4.patch
Patch1:		%{name}-0.9.3-build-flac.patch
Patch2:		%{name}-0.9.3-lib64.patch
BuildRoot:	%_tmppath/%{name}-buildroot
BuildRequires:	png-devel jpeg-devel libqt-devel pkgconfig
BuildRequires:	libalsa-devel jackit-devel libaudiofile-devel libsndfile-devel
BuildRequires:  libflac-devel libflac++-devel
BuildRequires:	desktop-file-utils

%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%prep
%setup -q
%patch0 -p0 -b .g++4
%patch1 -p0 -b .buildflac
%patch2 -p0 -b .lib64

%build
QTDIR=%{_prefix}/lib/qt3
export QTDIR
%configure2_5x
# doesn't seem to like parallel build
make

# fixed permissions
%__chmod 644 data/doc/tutorial_fr.docbook
%__chmod 644 data/doc/manual_fr.docbook

%install
%__rm -rf %buildroot
%makeinstall

perl -pi -e 's,/usr/share/%{name}/data/img/gray/icon64.png,%{name},g' %buildroot%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

#icons
%__mkdir_p %buildroot%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
%__cp data/img/gray/icon48.png %buildroot%_iconsdir/hicolor/48x48/apps/%{name}.png
%__cp data/img/gray/icon32.png %buildroot%_iconsdir/hicolor/32x32/apps/%{name}.png
%__cp data/img/gray/icon16.png %buildroot%_iconsdir/hicolor/16x16/apps/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/%name.desktop
%{_libdir}/%name
%{_datadir}/%name
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
