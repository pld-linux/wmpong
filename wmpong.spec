Summary:	Self playing pong game for WindowMaker Dock
Summary(pl):	Samograj�cy si� ping pong dla Doku WindowMakera
Name:		wmpong
Version: 	0.3
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	%{name}-%{version}-1.tar.gz
Source1:	wmpong.desktop
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
It's completely useless except for brainless entertainment value. 
It's a self playing pong game for WindowMaker Dock.


%description -l pl
Program ten jest ca�kowicie bezu�yteczny. Przeznaczony dla Doku
WindowMakera, graj�cy si� sam ping-pong.

%prep
%setup -q -n %{name}.app

%build
make -C %{name} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},/usr/X11R6/share/applnk/DockApplets} 
install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

gzip -9nf BUGS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,ChangeLog,README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}

/usr/X11R6/share/applnk/DockApplets/wmpong.desktop