Summary:	Self playing pong game for WindowMaker Dock
Summary(pl):	Samograj±cy siê ping pong dla Doku WindowMakera
Name:		wmpong
Version: 	0.3
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	%{name}-%{version}-1.tar.gz
Source1:	wmpong.desktop
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
It's completely useless except for brainless entertainment value. 
It's a self playing pong game for WindowMaker Dock.


%description -l pl
Program ten jest ca³kowicie bezu¿yteczny. Przeznaczony dla Doku
WindowMakera, graj±cy siê sam ping-pong.

%prep
%setup -q -n %{name}.app

%build
make -C %{name} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},/etc/X11/applnk/DockApplets} 
install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf BUGS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,ChangeLog,README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}

/etc/X11/applnk/DockApplets/wmpong.desktop

%changelog
* Tue May 25 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.3-1]
- initial RPM release.
