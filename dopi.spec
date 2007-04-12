%define name dopi
%define version 0.3.4
%define release %mkrel 2

Summary: Song uploader for the Apple iPod
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.snorp.net/files/dopi/%{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://www.snorp.net/log/dopi/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: ipod-sharp
BuildRequires: glade-sharp2
BuildRequires: glib2-devel
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils
#BuildRequires: gnome-common intltool

%description
Dopi is an application that allows you to update the songs stored on
your Apple iPod®, similar to gtkpod.

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/%name/* %buildroot%_libdir/%name/
perl -pi -e "s^%_prefix/lib^%_libdir^" %buildroot%_bindir/%name
%endif
rm -f %buildroot%_libdir/%name/libbacon*a %buildroot%_libdir/%name/ipod-sharp*
ln -s %_prefix/lib/ipod-sharp/ipod-sharp* %buildroot%_libdir/%name/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound;Audio;Player" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/%name
%_libdir/%name
%_datadir/applications/%name.desktop


