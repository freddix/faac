Summary:	Freeware Advanced Audio Codec
Name:		faac
Version:	1.28
Release:	6
License:	LGPL v2.1+
Group:		Applications/Sound
Source0:	http://heanet.dl.sourceforge.net/faac/%{name}-%{version}.tar.gz
# Source0-md5:	80763728d392c7d789cde25614c878f6
Patch0:		%{name}-mp4v2-1.9.patch
Patch1:		%{name}-mp4v2-2.0.0.patch
URL:		http://www.audiocoding.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mp4v2-devel
BuildRequires:	sed
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAAC is an ISO/MPEG 2/4 AAC encoder library developed for the Freeware
Advanced Audio Coding project.

%package libs
Summary:	Freeware Advanced Audio Codec library
Group:		Libraries

%description libs
FAAC is an ISO/MPEG 2/4 AAC encoder library developed for the Freeware
Advanced Audio Coding project.

%package devel
Summary:	Header files for faac library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for faac library.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/faac.1*

%files libs
%defattr(644,root,root,755)
%doc ChangeLog README TODO docs/faac.html
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/libfaac.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

