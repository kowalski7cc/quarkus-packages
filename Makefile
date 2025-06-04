VERSION = 3.20.1
BASE = quarkus
NAME =  $(BASE)-$(VERSION)
BUILDDIR=$(shell rpm --eval '%_topdir')

RPMBUILD=rpmbuild -D "version $(VERSION)"

install:
	install -D -m 644 lib/quarkus-cli-$(VERSION)-runner.jar $(DESTDIR)/usr/lib64/quarkus/quarkus-cli-$(VERSION)-runner.jar
	install -D -m 755 bin/quarkus $(DESTDIR)/usr/bin/quarkus

rpm:
	spectool -g -R quarkus.spec
	$(RPMBUILD) -bb --clean quarkus.spec