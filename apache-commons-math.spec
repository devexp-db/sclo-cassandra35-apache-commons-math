%global short_name commons-math3

Name:             apache-commons-math
Version:          3.4
Release:          1%{?dist}
Summary:          Java library of lightweight mathematics and statistics components
Group:            Development/Libraries
License:          ASL 1.1 and ASL 2.0 and BSD
URL:              http://commons.apache.org/math/
Source0:          http://www.apache.org/dist/commons/math/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
%if 0%{?fedora} >= 21
BuildRequires:    mvn(org.jacoco:jacoco-maven-plugin) >= 0.7.0
%endif
Requires:         jpackage-utils
BuildArch:        noarch

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in the
Java programming language or Commons Lang.


%package javadoc
Summary:          Javadoc for %{name}
Group:            Documentation

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "org.apache.commons:%{short_name}" "%{short_name}:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

# Disable Jacoco Maven plugin for Fedora releases having jacoco < 0.7.0
%if 0%{?fedora} < 21
rm src/site/resources/profile.jacoco
%endif

# Disable maven-jgit-buildnumber-plugin plugin (not available in Fedora)
%pom_remove_plugin ru.concerteza.buildnumber:maven-jgit-buildnumber-plugin


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Mon Jan 05 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.4-1
- Update to 3.4

* Fri Jun 13 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3-1
- Update to 3.3
- Drop apache-commons-math-3.2-RHBZ1084441.patch (fixed in 3.3)
- Drop apache-commons-math-3.2-JDK8.patch (Java 8 support enabled in 3.3)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2-4
- Fix RHBZ #1084441 (see
  https://issues.apache.org/jira/browse/MATH-1057)
- Disable unit test checking that all StrictMath methods are reimplemented in
  commons-math

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.2-4
- Use Requires: java-headless rebuild (#1067528)

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 3.2-3
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2-1
- Update to 3.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.1.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Sun Dec 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1-1
- Update to 3.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0-1
- Update to 3.0

* Mon Jan 16 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2-3
- Add missing apache-rat-plugin dependency
- Use Maven 3
- Spec cleanup

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2-1
- Update to 2.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Mat Booth <fedora@matbooth.co.uk> 2.1-3
- Drop versioned jars and javadocs, fixes F15 upgrade path.

* Fri Oct 22 2010 Chris Spike <chris.spike@arcor.de> 2.1-2
- Fixed maven-surefire-plugin BR for F14

* Fri Oct 22 2010 Chris Spike <chris.spike@arcor.de> 2.1-1
- Updated to 2.1
- Removed dependency on main package for -javadoc subpackage
- Fixed maven depmap entry
- Added jarfile symlinks (rhbz#612455)
- Added javadoc symlinks
- Added license file to -javadoc subpackage

* Wed Feb  3 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 2.0-6
- Add missing %%post/%%postun Requires
- Use macro %%{_mavendepmapfragdir} instead of %%{_datadir}/maven2/pom
- Unown directories %%{_mavenpomdir} and %%{_mavendepmapfragdir}

* Wed Jan 20 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 2.0-5
- Drop duplicate BuildRequires maven2

* Fri Jan  8 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 2.0-4
- Update description
- Add ASL 1.1 and BSD to License tag

* Thu Jan  7 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 2.0-3
- Change RPM name from "jakarta-commons-math" to "apache-commons-math"

* Sun Jan  3 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 2.0-2
- Update Summary tag

* Mon Dec 28 2009 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 2.0-1
- Initial RPM release
