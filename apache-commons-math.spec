%global base_name math
%global short_name commons-%{base_name}

Name:             apache-%{short_name}
Version:          2.2
Release:          3%{?dist}
Summary:          Java library of lightweight mathematics and statistics components

Group:            Development/Libraries
License:          ASL 1.1 and ASL 2.0 and BSD
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:           %{name}-2.2-remove_clirr_from_pom.patch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
Requires:         java >= 1:1.6.0
Requires:         jpackage-utils
BuildArch:        noarch

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in the
Java programming language or Commons Lang.


%package javadoc
Summary:          Javadoc for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1 -b .remove_clirr_from_pom


%build
mvn-rpmbuild install javadoc:javadoc


%install
# jars
install -Dpm 0644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
pushd $RPM_BUILD_ROOT%{_javadir}/
ln -s %{name}.jar %{short_name}.jar
popd

# pom
install -dm 0755 $RPM_BUILD_ROOT%{_mavenpomdir}/
install -pm 0644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -dm 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/api*/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/


%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
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
