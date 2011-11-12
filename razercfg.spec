Name:		razercfg
Version:	0.17
Release:	1
Summary:	This is the next generation Razer device configuration tool bringing the Razer gaming experience to the free OpenSource world.
                                                                                
Group:		System/Configuration/Hardware
License:        GPLv2
URL:		http://bu3sch.de/cms/index.php/razer-nextgen-config-tool
Source0:	http://bu3sch.de/razercfg/%{name}-%{version}.tar.bz2	
Source1:	razerd
BuildRequires:	python-qt4
BuildRequires:	cmake
BuildRequires:	libusb1-devel
BuildRequires:	python-devel
Patch0:		libdir_64_fix.patch

%description
This is the next generation Razer device configuration tool bringing the Razer gaming experience to the free OpenSource world.
This utility is a replacement for the old deathaddercfg tool.
The tool architecture is based on "razerd", which is a background daemon doing all of the lowlevel privileged hardware accesses. 
The user interface tools are "razercfg", a commandline tool; and "qrazercfg", a QT4 based graphical device configuration tool (see screenshot below). 

%prep
%setup -q
%patch0 -p1

%build
cmake .
%make
#%cmake

%install
#cd build/
%makeinstall_std

mkdir -p %{buildroot}%{_initrddir}/

%{__install} -m 0755 %{SOURCE1} -D %{buildroot}%{_initrddir}/razerd

%post
%_post_service razerd

%preun
%_preun_service razerd

%files
%doc COPYING README
%{_bindir}/%{name}
%{_bindir}/pyrazer.py
%{_bindir}/qrazercfg
%{_prefix}/sbin/razerd
%{_libdir}/librazer.so
%{_sysconfdir}/pm/sleep.d/50-razer
%{_initrddir}/razerd
%{_sysconfdir}/udev/rules.d/01-razer-udev.rules
