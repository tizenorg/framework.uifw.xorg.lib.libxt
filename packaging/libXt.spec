Summary: X.Org X11 libXt runtime library
Name: libXt
Version: 1.1.2
Release: 2
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(xproto) pkgconfig(x11) pkgconfig(sm)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXt runtime library

%package devel
Summary: X.Org X11 libXt development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxt-devel

%description devel
X.Org X11 libXt development package

%prep
%setup -q

%build
# FIXME: Work around pointer aliasing warnings from compiler for now
export CFLAGS="${CFLAGS} $RPM_OPT_FLAGS -fno-strict-aliasing"
%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed" \
           --with-appdefaultdir=/etc/X11/app-defaults \
           --with-xfile-search-path="/usr/lib/X11/%L/%T/%N%S:/usr/lib/X11/%l/%T/%N%S:/usr/lib/X11/%T/%N%S:/etc/X11/%L/%T/%N%C%S:/etc/X11/%l/%T/%N%C%S:/etc/X11/%T/%N%C%S:/etc/X11/%L/%T/%N%S:/etc/X11/%l/%T/%N%S:/etc/X11/%T/%N%S"

make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_libdir}/libXt.so.6
%{_libdir}/libXt.so.6.0.0
%dir %{_datadir}/X11/app-defaults

%files devel
%defattr(-,root,root,-)
#%{_datadir}/doc/%{name}
%{_includedir}/X11/CallbackI.h
%{_includedir}/X11/Composite.h
%{_includedir}/X11/CompositeP.h
%{_includedir}/X11/ConstrainP.h
%{_includedir}/X11/Constraint.h
%{_includedir}/X11/ConvertI.h
%{_includedir}/X11/Core.h
%{_includedir}/X11/CoreP.h
%{_includedir}/X11/CreateI.h
%{_includedir}/X11/EventI.h
%{_includedir}/X11/HookObjI.h
%{_includedir}/X11/InitialI.h
%{_includedir}/X11/Intrinsic.h
%{_includedir}/X11/IntrinsicI.h
%{_includedir}/X11/IntrinsicP.h
%{_includedir}/X11/Object.h
%{_includedir}/X11/ObjectP.h
%{_includedir}/X11/PassivGraI.h
%{_includedir}/X11/RectObj.h
%{_includedir}/X11/RectObjP.h
%{_includedir}/X11/ResConfigP.h
%{_includedir}/X11/ResourceI.h
%{_includedir}/X11/SelectionI.h
%{_includedir}/X11/Shell.h
%{_includedir}/X11/ShellI.h
%{_includedir}/X11/ShellP.h
%{_includedir}/X11/StringDefs.h
%{_includedir}/X11/ThreadsI.h
%{_includedir}/X11/TranslateI.h
%{_includedir}/X11/VarargsI.h
%{_includedir}/X11/Vendor.h
%{_includedir}/X11/VendorP.h
%{_includedir}/X11/Xtos.h
%{_libdir}/libXt.so
%{_libdir}/pkgconfig/xt.pc
#%{_mandir}/man3/*.3*
