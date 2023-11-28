Name:           quarkus
Version:        3.5.3
Release:        %autorelease
Summary:        Quarkus: Supersonic Subatomic Java.

License:        Apache-2.0
Source0:        https://github.com/quarkusio/quarkus/releases/download/%{version}/quarkus-cli-%{version}.tar.gz
BuildArch:      noarch

%description
Quarkus is a Cloud Native, (Linux) Container First framework for writing Java applications.

%prep
%setup -q -c -n %{name}-%{version}

%install
%{__install} -D -m 0644 quarkus-cli-3.5.3/lib/quarkus-cli-%{version}-runner.jar %{buildroot}%{_datadir}/quarkus/lib/quarkus-cli-%{version}-runner.jar
%{__install} -D -m 0755 quarkus-cli-3.5.3/bin/quarkus %{buildroot}%{_datadir}/quarkus/bin/quarkus

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
