PACKAGE := python-linux-procfs
VERSION := $(shell rpm -q --qf '%{VERSION}' --specfile rpm/SPECS/$(PACKAGE).spec)

bz2:
	git archive --format=tar HEAD | bzip2 -9 > rpm/SOURCES/$(PACKAGE)-$(VERSION).tar.bz2

rpm: bz2
	rpmbuild -ba --define "_topdir $(PWD)/rpm" rpm/SPECS/$(PACKAGE).spec
