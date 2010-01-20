%global base_name math
%global short_name commons-%{base_name}

Name:           apache-commons-math
Version:        2.0
Release:        4%{?dist}
Summary:        Java library of lightweight mathematics and statistics components

Group:          Development/Libraries
License:        ASL 1.1 and ASL 2.0 and BSD
URL:            http://commons.apache.org/math/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Cannot build with gcj, gjdoc currently blocks this (bug similar to
# rhbz#510243)
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  junit4
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
BuildArch:      noarch

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in the
Java programming language or Commons Lang.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    install javadoc:javadoc


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -p pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.maven %{name} %{version} JPP %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post
%update_maven_depmap


%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_datadir}/maven2/poms
%{_javadir}/*.jar
%{_mavendepmapfragdir}


%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
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
