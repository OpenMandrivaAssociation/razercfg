%define major 1
%define libname %mklibname razer %{major}

Name:		razercfg
Version:	0.43
Release:	1
Summary:	Razer device configuration tool
Group:		System/Configuration/Hardware
License:	GPLv2
URL:		https://bues.ch/cms/hacking/razercfg.html
Source0:	https://bues.ch/razercfg/%{name}-%{version}.tar.bz2
Source1:	razerd.service
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	python-qt5-devel
BuildRequires:	cmake
BuildRequires:	pkgconfig(python)

Requires:	python-qt5-core
Requires:	python-qt5-gui
Requires:	python-qt5-network
Requires:	python-qt5-widgets
Patch0:		libdir_64_fix.patch

%description
This is the next generation Razer device configuration tool
bringing the Razer gaming experience to the free open source world.
This utility is a replacement for the old deathaddercfg tool.
The tool architecture is based on "razerd", which is a background
daemon doing all of the lowlevel privileged hardware accesses.
The user interface tools are "razercfg", a commandline tool;
and "qrazercfg", a QT4 based graphical device configuration tool.

%package -n %{libname}
Summary:        Razer device configuration tool
Group:          System/Libraries
Conflicts:      %{name} < 0.39-4
Obsoletes:      %{_lib}%{name}1 < 0.39-3

%description -n %{libname}
This is the next generation Razer device configuration tool
bringing the Razer gaming experience to the free open source world.
This utility is a replacement for the old deathaddercfg tool.
The tool architecture is based on "razerd", which is a background
daemon doing all of the lowlevel privileged hardware accesses.
The user interface tools are "razercfg", a commandline tool;
and "qrazercfg", a QT4 based graphical device configuration tool.

%prep
%setup -q
%autopatch -p1

%build
%cmake
%make_build

%install
#cd build/
%make_install -C build

mkdir -p %{buildroot}%{_unitdir}/

%{__install} -m 0755 %{SOURCE1} -D %{buildroot}%{_unitdir}/razerd.service
#{__install} -d %{buildroot}%{_sbindir}
#mv %{buildroot}%{_bindir}/razerd %{buildroot}%{_sbindir}/razerd

rm -f %{buildroot}/%{_libdir}/*.so

%post
%_post_service razerd.service

%preun
%_preun_service razerd.service

%files
%doc COPYING README* HACKING*
%{_bindir}/razer*
%{_bindir}/qrazercfg*
%{_unitdir}/razerd.service
%{_sysconfdir}/pm/sleep.d/50-razer
%{_sysconfdir}/udev/rules.d/80-razer.rules
%{python3_sitelib}/*
%{_datadir}/applications/razercfg.desktop
%{_iconsdir}/hicolor/scalable/*
%{_prefix}/lib/tmpfiles.d/razerd.conf

%files -n %{libname}
%{_libdir}/*.so.%{major}{,.*}
