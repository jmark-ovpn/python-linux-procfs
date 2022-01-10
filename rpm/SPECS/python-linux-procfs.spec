%if 0%{?fedora}
%global with_python3 1
%else
%global without_python3 1
%endif

Name: python-linux-procfs
Version: 0.7.0
Release: 1%{?dist}
License: GPLv2
Summary: Linux /proc abstraction classes
Group: System Environment/Libraries
Source: https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
URL: https://rt.wiki.kernel.org/index.php/Tuna
BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools
%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%global _description\
Abstractions to extract information from the Linux kernel /proc files.

%description %_description

%package -n python2-linux-procfs
Summary: %summary
%{?python_provide:%python_provide python2-linux-procfs}

Requires: python-six

%description -n python2-linux-procfs %_description

%if 0%{?with_python3}
%package -n python3-linux-procfs
Summary: %summary
%{?python_provide:%python_provide python3-linux-procfs}

Requires: python3-six

%description -n python3-linux-procfs %_description
%endif

%prep
%autosetup -p1

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
rm -rf %{buildroot}
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%clean
rm -rf %{buildroot}

%files -n python2-linux-procfs
%defattr(0755,root,root,0755)
%{python2_sitelib}/procfs/
%if 0%{?without_python3}
%{_bindir}/pflags
%endif
%defattr(0644,root,root,0755)
%{python2_sitelib}/python_linux_procfs*.egg-info
%license COPYING

%if 0%{?with_python3}
%files -n python3-linux-procfs
%defattr(0755,root,root,0755)
%{_bindir}/pflags
%{python3_sitelib}/procfs/
%defattr(0644,root,root,0755)
%{python3_sitelib}/python_linux_procfs*.egg-info
%license COPYING
%endif

%changelog
* Mon Jan 10 2022 John Kacur <jkacur@redhat.com> - 0.7.0-1
- python-linux-procfs: Add tar.xz and asc files to gitignore
- python-linux-procfs: Fix traceback with non-utf8 chars in the
  /proc/PID/cmdline
- python-linux-procfs: Propagate error to user if a pid is completed
- python-linux-procfs: pflags: Handle pids that completed
- python-linux-procfs: Makefile: Add ctags
- python-linux-procfs: Remove procfs/sysctl.py
- python-linux-procfs: Various clean-ups
- python-linux-procfs: Fix UnicodeDecodeError

* Mon Jan 11 2021 John Kacur <jkacur@redhat.com> - 0.6.3-1
- python-linux-procfs: Fix more spacing problems with procfs.py
- python-linux-procfs: procfs.py: Simplify is_s390
- python-linux-procfs: procfs.py: Fix a few more style problems

* Mon Jun 22 2020 John Kacur <jkacur@redhat.com> - 0.6.2-1
- Add bitmasklist_test
- clean-ups for recent python formating regarding spacing, tabs, etc
- Fix to parse the number of cpus correctly on s390(x)

* Fri Jan 11 2019 Jiri Kastner <jkastner@redhat.com> - 0.6.1-1
- python3 fixes

* Thu Aug  9 2018 Jiri Kastner <jkastner@redhat.com> - 0.6-1
- moved cannot)set*affinity calls from tuna

* Tue Nov 21 2017 Jiri Kastner <jkastner@redhat.com> - 0.5.1-1
- missed snippet in specfile for python2 only
- added scripts to setup.py, pflags renamed and added to setup.py

* Mon Nov 20 2017 Jiri Kastner <jkastner@redhat.com> - 0.5-1
- added python3 support

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
