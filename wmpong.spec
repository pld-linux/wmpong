Summary:	Self playing pong game for WindowMaker Dock
Summary(pl.UTF-8):   Grający sam ze sobą ping pong dla Doku WindowMakera
Name:		wmpong
Version:	0.3
Release:	6
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://ftp.windowmaker.org/pub/contrib/srcs/games/%{name}-%{version}-1.tar.gz
# Source0-md5:	d2f7fec0b89697ebaa165eba605456b3
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
It's completely useless except for brainless entertainment value. It's
a self playing pong game for WindowMaker Dock.

%description -l pl.UTF-8
Program ten jest całkowicie bezużyteczny. Przeznaczony dla Doku
WindowMakera, grający sam ze sobą ping-pong.

%prep
%setup -q -n %{name}.app

%build
%{__make} -C %{name} \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/wmpong.desktop
