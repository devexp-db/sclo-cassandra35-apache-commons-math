%{?scl:%scl_package apache-commons-math}
%{!?scl:%global pkg_name %{name}}

%global short_name commons-math3

Name:             %{?scl_prefix}apache-commons-math
Version:          3.4.1
Release:          2%{?dist}
Summary:          Java library of lightweight mathematics and statistics components
Group:            Development/Libraries
License:          ASL 1.1 and ASL 2.0 and BSD
URL:              http://commons.apache.org/math/
Source0:          http://www.apache.org/dist/commons/math/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    %{?scl_mvn_prefix}maven-local
BuildRequires:    %{?scl_mvn_prefix}mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    %{?scl_mvn_prefix}mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    %{?scl_mvn_prefix}mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:    %{?scl_mvn_prefix}mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:    junit

%if 0%{?fedora} >= 21
BuildRequires:    mvn(org.jacoco:jacoco-maven-plugin) >= 0.7.0
%endif
BuildArch:        noarch

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in the
Java programming language or Commons Lang.

%package javadoc
Summary:          Javadoc for %{pkg_name}
Group:            Documentation

%description javadoc
This package contains the API documentation for %{name}.

%prep
%{?scl_enable}
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "org.apache.commons:%{short_name}" "%{short_name}:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{pkg_name}

# Disable Jacoco Maven plugin for Fedora releases having jacoco < 0.7.0
%if 0%{?fedora} < 21 || 0%{?scl}
rm src/site/resources/profile.jacoco
%endif

# Disable maven-jgit-buildnumber-plugin plugin (not available in Fedora)
%pom_remove_plugin ru.concerteza.buildnumber:maven-jgit-buildnumber-plugin

# Try to remove parent
%pom_remove_parent

# remove some plugins
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-surefire-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin


%{?scl_disable}

%build
%{?scl_enable}
%mvn_build
%{?scl_disable}

%install
%{?scl_enable}
%mvn_install
%{?scl_disable}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Jul 27 2016 Tomas Repik <trepik@redhat.com> - 3.4.1-2
- removed parent, added missing dependencies

* Wed Jul 27 2016 Pavel Raiskup <praiskup@redhat.com> - 3.4.1-1
- sclize
