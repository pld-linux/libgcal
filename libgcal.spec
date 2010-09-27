Summary:	Library implementing the SSH protocol
Summary(pl.UTF-8):	Biblioteka implementująca protokół SSH
Name:		libgcal
Version:	0.9.6
Release:	0.1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://libgcal.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	f15690f016ec6d41791cbe2b0149cf1b
URL:		http://code.google.com/p/libgcal/
BuildRequires:	cmake >= 2.6.0
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package devel
Summary:	Header files for libgcal library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgcal
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libgcal library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgcal.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgcal.so
%{_includedir}/libgcal
%{_pkgconfigdir}/libgcal.pc
