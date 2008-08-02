%define base_name       superkaramba-theme
%define theme_name      cynapses_karamba
%define name            %{base_name}-%{theme_name}
%define version         2.0.alpha
%define release         %mkrel 5
%define aname		sys_mon
Name:	%{name}
Version:	%{version}
Release:        %{release}
Summary:        Monitoring theme for superkaramba
License:        GPL
Group:          Monitoring
Source:         11405-%{theme_name}.tar.bz2      
URL:            http://www.cynapses.org/
Requires:       superkaramba >= 0.35
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
This is a desktop applet that displays system informations.


%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}

%build

%install
mkdir -p  %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf *  %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name}
chmod 755 %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name}/scripts/mails_pop3.pl
chmod 755 %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name}/scripts/osinfo.sh

 
%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ $1 = 1 ]; then
echo "THEME path=%{theme_name}/%{aname}.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
fi

%postun
if [ $1 = 0 ]; then
cat %{_datadir}/apps/superkaramba/themes/default.theme | grep -v "%{theme_name}" > %{_datadir}/apps/superkaramba/themes/default.theme
exit 0
fi

%files
%defattr(-,root,root)
%doc ChangeLog
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*


