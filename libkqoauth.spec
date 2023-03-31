%define	major	0
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname %{oname} -d
%define	oname kqoauth

%define _disable_lto 1

Name:           libkqoauth
Version:        0.98
Release:        5
Summary:        C++/Qt OAuth 1.0 RFC 5849 library
License:        LGPLv3+
Group:          System/Libraries
Url:            https://github.com/kypeli/kQOAuth
# https://github.com/kypeli/kQOAuth/archive/%%{version}.tar.gz
Source0:        kQOAuth-%{version}.tar.gz
Patch0:         libdir.patch

BuildRequires:  pkgconfig(QtNetwork) >= 4.7

%description
kQOAuth is a OAuth 1.0 library written for Qt in C++.
The goals for the library have been to provide 
easy integration to existing
Qt applications utilizing Qt signals describing 
the OAuth process, and to provide a
convenient approach to OAuth authentication. 
kQOAuth has support for retrieving the user 
authorization from the service 
provider's website. kQOAuth will open 
the user's web browser to the 
authorization page, give a local URL as the 
callback URL and setup a HTTP 
server on this address to listen for
the reply from the service and then 
process it.

%package -n %{libname}
Summary:        C++/Qt OAuth 1.0 RFC 5849 library
Group:          System/Libraries

%description    -n %{libname}
kQOAuth is a OAuth 1.0 library written for Qt in C++.
The goals for the library have been to provide 
easy integration to existing
Qt applications utilizing Qt signals describing 
the OAuth process, and to provide a
convenient approach to OAuth authentication. 
kQOAuth has support for retrieving the user 
authorization from the service 
provider's website. kQOAuth will open 
the user's web browser to the 
authorization page, give a local URL as the 
callback URL and setup a HTTP 
server on this address to listen for
the reply from the service and then 
process it.

%files -n %{libname}
%doc COPYING CHANGELOG README*
%{_libdir}/%{name}.so.*

#----------------------------------------------
%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/C 
Requires:       %{libname} = %{EVRD}

%description   -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files  -n %{devname}
%doc COPYING CHANGELOG README*
%{_includedir}/QtKOAuth/
%{_libdir}/%{name}.so
%{_libdir}/%{name}.prl
%{_libdir}/pkgconfig/kqoauth.pc
%{_prefix}/lib/qt4/mkspecs/features/kqoauth.prf



%prep
%setup -q -n kQOAuth-%{version}
%patch0 -p1

%build
`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
      PREFIX=%{_prefix} \
      KQOAUTH_LIBDIR=%{_libdir} \
      QMAKE_STRIP="" \
      QMAKE_CXXFLAGS+="%{optflags}"
%make

%install
%make_install INSTALL_ROOT=%{buildroot}




