Summary:	Start runlevel scripts in parallel
Summary(pl.UTF-8):	Równoległe uruchamianie skryptów startowych
Name:		startpar
Version:	0.50
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	52440e5d7cb9b2b14effafebf1361621
Patch0:		%{name}-suse.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
startpar is used to run multiple run-level scripts in parallel. The
degree of parallelism on one CPU can be set with the -p option, the
default is full parallelism. An argument to all of the scripts can be
provided with the -a option. Processes block by pending I/O will
weighting by the factor 800. To change this factor the option -i can
be used to specify an other value.

%description -l pl.UTF-8
startpar służy do równoległego uruchamiania wielu skryptów startowych
dla danego poziomu działania systemu. Stopień równoległości dla
jednego procesora można ustawić opcją -p, domyślna jest pełne
zrównoleglenie. Za pomocą opcji -a można przekazać argument do
wszystkich skryptów. Procesy blokowane przez oczekiwanie na we/wy są
uwzględniane z wagą 800; można zmienić ten współczynnik za pomocą
opcji -i.

%prep
%setup -q
%patch -P0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/startpar
%{_mandir}/man8/startpar.8*
