Name:		xloadimage
Summary: 	Image viewer and processor
Version:	4.1
Release:	1
License:	MIT
Group:		Graphics
URL:		http://www.frostbytes.com/~jimf/xloadimage.html
Source0:	ftp://ftp.x.org/R5contrib/%{name}.%{version}.tar.gz
# Patches 0-18 come from Debian 4.1-16.1
# Many thanks to all those who have done work on this package over the years
Patch0:		01_libjpeg-support.dpatch
Patch1:		02_png-support.dpatch
Patch2:		03_security-strfoo.dpatch
Patch3:		04_previous-image.dpatch
Patch4:		05_idelay-manpage.dpatch
Patch5:		06_-Wall-cleanup.dpatch
Patch6:		07_SYSPATHFILE.dpatch
Patch7:		08_manpage-config-path.dpatch
Patch8:		09_xloadimagerc-path.dpatch
Patch9:		10_config.c-HOME-fix.dpatch
Patch10:	11_fork-implies-quiet.dpatch
Patch11:	12_fix-tile.dpatch
Patch12:	13_varargs-is-obsolete.dpatch
Patch13:	14_errno-not-extern.dpatch
Patch14:	15_CAN-2005-0638.dpatch
Patch15:	16_CAN-2005-0639.dpatch
Patch16:	17_security-sprintf.dpatch
Patch17:	18_manpage_fixes.dpatch
Patch18:	19_fix_root_c_resource_leak.dpatch
Patch19:	xloadimage-4.1-ignore-dummy-copyright-variables.patch
Patch20:	xloadimage-4.1-bracketfix.patch
Patch21:	xloadimage-4.1-png-pkg-config.patch
Patch22:	xloadimage-4.1-libtiff4.patch
Patch23:	xloadimage-4.1-png-1.5.patch
Patch24:	xloadimage-4.1-fix-mem-leak.patch
Patch25:	xloadimage-4.1-sub-second-delay.patch

BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(ice)
Obsoletes:  xli < 20061110-21
Provides: xli = 20061110-21

%description
Xloadimage is a utility which will view many different types of images 
under X11, load images onto the root window, or dump processed images 
into one of several image file formats. The current version can read 
many different image file types.

A variety of options are available to modify images prior to viewing. 
These options include clipping, dithering, depth reduction, zoom (either 
X or Y axis independently or both at once), brightening or darkening, 
and image merging. When applicable, these options are done automatically 
(eg a color image to be displayed on a monochrome screen will be 
dithered automatically). 

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1 -b .png-pkg-config
%patch22 -p1 -b .tiff4
%patch23 -p1 -b .png15
%patch24 -p1 -b .fix-mem-leak
%patch25 -p1 -b .sub-second-delay

chmod +x configure

%build
%configure
make_build

%install
# First, the binaries:
mkdir -p %{buildroot}%{_bindir}
install -m 0755 uufilter %{buildroot}%{_bindir}
install -m 0755 xloadimage %{buildroot}%{_bindir}
# Next, the symlinks
pushd %{buildroot}%{_bindir}
ln -s xloadimage xsetbg
ln -s xloadimage xview
popd
# The configuration file
mkdir -p %{buildroot}%{_sysconfdir}/X11/
install -m 0644 xloadimagerc %{buildroot}%{_sysconfdir}/X11/Xloadimage
# Now, the man pages
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 0644 xloadimage.man %{buildroot}%{_mandir}/man1/xloadimage.1x
install	-m 0644 uufilter.man %{buildroot}%{_mandir}/man1/uufilter.1x
# And some copies for the symlinks (we can't really make symlinks here because of how rpm 
# compresses man pages)
cp -a %{buildroot}%{_mandir}/man1/xloadimage.1x %{buildroot}%{_mandir}/man1/xsetbg.1x
cp -a %{buildroot}%{_mandir}/man1/xloadimage.1x %{buildroot}%{_mandir}/man1/xview.1x

%files
%doc README mit.cpyrght
%{_bindir}/uufilter
%{_bindir}/xloadimage
%{_bindir}/xsetbg
%{_bindir}/xview
%config(noreplace) %{_sysconfdir}/X11/Xloadimage
%{_mandir}/man1/*
