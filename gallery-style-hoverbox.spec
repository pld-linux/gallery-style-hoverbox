%define		_style		hoverbox
Summary:	Hoverbox CSS style for Gallery2
Summary(pl.UTF-8):   Styl CSS Hoverbox dla Gallery2
Name:		gallery-style-%{_style}
Version:	1
Release:	1
License:	GPL
Group:		Applications/Publishing
#Source0:	http://sonspring.com/files/%{_style}.zip
Source0:	http://gallery.menalto.com/files/g2_carbon_%{_style}.zip
# Source0-md5:	1a933624ddfd8b3b1af74859e93138d6
URL:		http://sonspring.com/journal/hoverbox-image-gallery
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	gallery >= 2.1.0
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery

%description
Super light-weight (8kB) roll-over photo gallery that uses nothing but
CSS.

%description -l pl.UTF-8
Bardzo lekka (8kB) galeria fotografii używająca wyłącznie CSS-a.

%prep
%setup -q -n %{_style}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/%{_style}

install *.css $RPM_BUILD_ROOT%{_appdir}/%{_style}
install *.gif $RPM_BUILD_ROOT%{_appdir}/%{_style}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_appdir}/%{_style}
%{_appdir}/%{_style}/*.css
%{_appdir}/%{_style}/*.gif
