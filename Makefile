PACKAGE := python-linux-procfs
VERSION := $(shell rpm -q --qf '%{VERSION}' --specfile rpm/SPECS/$(PACKAGE).spec)

rpmdirs:
	@[ -d rpm/BUILD ]   || mkdir rpm/BUILD
	@[ -d rpm/RPMS ]    || mkdir rpm/RPMS
	@[ -d rpm/SRPMS ]   || mkdir rpm/SRPMS
	@[ -d rpm/SOURCES ] || mkdir rpm/SOURCES

bz2: rpmdirs
	git archive --format=tar --prefix=$(PACKAGE)-$(VERSION)/ HEAD | \
	bzip2 -9 > rpm/SOURCES/$(PACKAGE)-$(VERSION).tar.bz2

rpm: bz2 rpmdirs
	rpmbuild -ba --define "_topdir $(PWD)/rpm" rpm/SPECS/$(PACKAGE).spec

bz2dev: rpmdirs
	@mkdir -p /tmp/$(PACKAGE)-$(VERSION)
	@tar cf - `cat MANIFEST` | (cd /tmp/$(PACKAGE)-$(VERSION) ; tar xf -)
	@(cd /tmp; tar cf - $(PACKAGE)-$(VERSION)) | bzip2 -9 > rpm/SOURCES/$(PACKAGE)-$(VERSION).tar.bz2

rpmdev: bz2dev rpmdirs
	rpmbuild -ba --define "_topdir $(PWD)/rpm" rpm/SPECS/$(PACKAGE).spec

rpmclean:
	@rm -f rpm/RPMS/*/$(PACKAGE)-$(VERSION)-*.rpm
	@rm -f rpm/SRPMS/$(PACKAGE)-$(VERSION)-*.src.rpm
	@rm -f rpm/SOURCES/$(PACKAGE)-$(VERSION).tar.bz2
	@rm -rf rpm/BUILD/$(PACKAGE)-$(VERSION)*

pyclean:
	@find . -type f \( -name \*~ -o -name \*.pyc \) -delete

.PHONY: tags
tags:
	ctags -R --extra=+fq --python-kinds=+cfmvi

.PHONY: cleantags
cleantags:
	rm -f tags

clean: pyclean rpmclean cleantags
