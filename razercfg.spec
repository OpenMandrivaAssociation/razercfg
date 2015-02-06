Name:		razercfg
Version:	0.19
Release:	2
Summary:	Razer device configuration tool
Group:		System/Configuration/Hardware
License:	GPLv2
URL:		http://bues.ch/cms/hacking/razercfg.html
Source0:	http://bues.ch/razercfg/%{name}-%{version}.tar.bz2
Source1:	razerd.service
BuildRequires:	python-qt4
BuildRequires:	cmake
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	python-devel
Patch0:		libdir_64_fix.patch

%description
This is the next generation Razer device configuration tool
bringing the Razer gaming experience to the free open source world.
This utility is a replacement for the old deathaddercfg tool.
The tool architecture is based on "razerd", which is a background
daemon doing all of the lowlevel privileged hardware accesses.
The user interface tools are "razercfg", a commandline tool;
and "qrazercfg", a QT4 based graphical device configuration tool.

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make

%install
#cd build/
%makeinstall_std -C build

mkdir -p %{buildroot}%{_unitdir}/

%{__install} -m 0755 %{SOURCE1} -D %{buildroot}%{_unitdir}/razerd.service

%post
%_post_service razerd.service

%preun
%_preun_service razerd.service

%files
%doc COPYING README
%{_bindir}/*
%{_sbindir}/razerd
%{_unitdir}/razerd.service
%{_libdir}/librazer.so
%{_sysconfdir}/pm/sleep.d/50-razer
%{_sysconfdir}/udev/rules.d/01-razer-udev.rules
