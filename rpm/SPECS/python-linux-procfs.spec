%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_ver: %define python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name: python-linux-procfs
Version: 0.4.11
Release: 1%{?dist}
License: GPLv2
Summary: Linux /proc abstraction classes
Group: System Environment/Libraries
Source: https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
URL: https://rt.wiki.kernel.org/index.php/Tuna
BuildArch: noarch
BuildRequires: python-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Abstractions to extract information from the Linux kernel /proc files.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp pflags-cmd.py %{buildroot}%{_bindir}/pflags

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/pflags
%{python_sitelib}/procfs/
%defattr(0644,root,root,0755)
%if "%{python_ver}" >= "2.5"
%{python_sitelib}/*.egg-info
%endif
%doc COPYING

%changelog
* Tue Sep 26 2017 Jiri Kastner <jkastner@redhat.com> - 0.4.11-1
- fixed rpmlint compliants (url, source)

* Thu Dec 22 2016 Jiri Kastner <jkastner@redhat.com> - 0.4.10-1
- fixed affinity parsing with cpu numbers greater than 31
- added test for fix above

* Thu Oct  8 2015 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.9-1
- Adds documentations to classes, more work to do on methods
- Fixes parsing of users in /proc/interrupts users field
- Fixes: https://bugzilla.redhat.com/show_bug.cgi?id=1245677

* Tue Jun 23 2015 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.8-1
- Support spaces in COMM names
- Fixes: https://bugzilla.redhat.com/show_bug.cgi?id=1232394

* Thu Jun 11 2015 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.7-1
- Fix pidstat.process_flag()
- Introduce pflags utility
- Parse IRQ affinities for !root
- Add PF_NO_SETAFFINITY const

* Wed Jun  5 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.6-1
- support for parsing cgroups
- support for parsing environ variables

* Mon May 10 2010 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.5-1
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=577365

* Mon Feb 10 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.4-1
- Even more fixes due to the fedora review process

* Mon Feb  9 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.3-1
- Fixups due to the fedora review process

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.2-1
- interrupts: Add find_by_user_regex
- process: Always set the "cmdline" array, even if empty
- pidstats: Remove dead processes in find_by_name()
- pidstats: Add process class to catch dict references for late parsing
- pidstats: Move the /proc/PID/{stat,status} parsing to classes
- pidstats: Introduce process_flags method

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4-1
- Per process flags needed by tuna

* Fri Jun 13 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.3-1
- Support CPU hotplug

* Mon Feb 25 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-1
- package created
