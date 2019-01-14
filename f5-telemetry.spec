Summary: F5 Telemetry Streaming
Version: 0.9.0
Name: %{_name}
Release: %{_release}
BuildArch: noarch
Group: Development/Tools
License: Commercial
Packager: F5 Networks <support@f5.com>

%description
Telemetry Streaming for BIG-IP

%define IAPP_INSTALL_DIR /var/config/rest/iapps/%{name}

%define _binaries_in_noarch_packages_terminate_build 0

%prep
cp -r %{main}/src/ %{_builddir}/src/
if [ -d "%{main}/node_modules" ] ; then cp -r %{main}/node_modules %{_builddir}/src/ ; fi
echo -n %{version}-%{release} > %{_builddir}/src/version

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{IAPP_INSTALL_DIR}
cp -r %{_builddir}/src/* $RPM_BUILD_ROOT%{IAPP_INSTALL_DIR}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{IAPP_INSTALL_DIR}
