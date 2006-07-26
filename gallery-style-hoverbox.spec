%define		_style		hoverbox
Summary:	Hoverbox css style for Gallery2
Name:		gallery-style-%{_style}
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/Publishing
Source0:	http://sonspring.com/files/%{_style}.zip
# Source0-md5:	e4ae8d050a8baa3205eca06c82cd0c0d
URL:		http://sonspring.com/journal/hoverbox-image-gallery
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	gallery >= 2.1.0
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery

%description
Super light-weight (8kb) roll-over photo gallery that uses nothing but CSS.

%prep
%setup -q -n %{_style}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/%{_style}

install css/*.css $RPM_BUILD_ROOT%{_appdir}/%{_style}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_appdir}/%{_style}
%{_appdir}/%{_style}/*.css
