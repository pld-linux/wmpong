Summary:	Self playing pong game for WindowMaker Dock
Summary(pl):	Graj±cy sam ze sob± ping pong dla Doku WindowMakera
Name:		wmpong
Version:	0.3
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://ftp.windowmaker.org/pub/contrib/srcs/games/%{name}-%{version}-1.tar.gz
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
It's completely useless except for brainless entertainment value. It's
a self playing pong game for WindowMaker Dock.

%description -l pl
Program ten jest ca³kowicie bezu¿yteczny. Przeznaczony dla Doku
WindowMakera, graj±cy sam ze sob± ping-pong.

%prep
%setup -q -n %{name}.app

%build
%{__make} -C %{name} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets} 

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf BUGS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}

#%{_applnkdir}/DockApplets/wmpong.desktop
