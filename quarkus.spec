Name:           quarkus
Version:        3.20.1
Release:        1
Summary:        Quarkus: Supersonic Subatomic Java.

License:        Apache-2.0
Source0:        https://github.com/quarkusio/quarkus/releases/download/%{version}/quarkus-cli-%{version}.tar.gz
BuildArch:      noarch

Requires:       (java-17-openjdk-headless or java-17-openjdk or java-21-openjdk-headless or java-21-openjdk)
Suggests:       maven

%description
Quarkus is a Cloud Native, (Linux) Container First framework for writing Java applications.

%prep
%setup -q -c -n %{name}-%{version}

%install
%{__install} -D -m 0644 quarkus-cli-%{version}/lib/quarkus-cli-%{version}-runner.jar %{buildroot}%{_datadir}/quarkus/lib/quarkus-cli-%{version}-runner.jar
%{__install} -D -m 0755 quarkus-cli-%{version}/bin/quarkus %{buildroot}%{_datadir}/quarkus/bin/quarkus

%post
# symlink /usr/bin/quarkus to /usr/share/quarkus/lib/quarkus
ln -s %{_datadir}/quarkus/bin/quarkus %{_bindir}/quarkus

%postun
%{__rm} -f %{_bindir}/quarkus

%changelog
%autochangelog

%files
%dir %{_datadir}/quarkus
%{_datadir}/quarkus/lib/quarkus-cli-%{version}-runner.jar
%{_datadir}/quarkus/bin/quarkus
