%define name dopi
%define version 0.3.4
%define svn 238
%define release %mkrel 2.%svn.1

Summary: Song uploader for the Apple iPod
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.snorp.net/files/dopi/%{name}-%{svn}.tar.bz2
Patch: dopi-238-desktopentry.patch
License: GPL
Group: Sound
Url: http://www.snorp.net/log/dopi/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: ipod-sharp
BuildRequires: glade-sharp2
BuildRequires: glib2-devel
BuildRequires: perl-XML-Parser
BuildRequires: gnome-common intltool

%description
Dopi is an application that allows you to update the songs stored on
your Apple iPod®, similar to gtkpod.

%prep
%setup -q -n %name
%patch -p0
./autogen.sh

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

# use the external package
rm -f %buildroot%_libdir/%name/taglib-sharp*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/%name
%_libdir/%name
%_datadir/applications/%name.desktop


