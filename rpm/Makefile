NAME       := python3-easylogconfig
SPEC       ?= $(NAME).spec
DOCKER     ?= 1
DOCKER_CMD ?= docker
VER        := $(shell awk '/Version:/ {print $$2}' $(SPEC))
ARCHIVE    := $(NAME)-$(VER).tar.gz
USERID     := $(shell id -u)
IMAGE      := builder-ol8_easyloconfig

ifeq ($(DOCKER),1)
CMD_PREFIX := $(DOCKER_CMD) run --rm -it -v $(PWD):/host:ro -v $(HOME)/rpmbuild:/home/builder/rpmbuild:rw $(IMAGE)
SPEC       := /host/$(SPEC)
endif

.PHONY: rpm clean

$(HOME)/rpmbuild:
	mkdir -p $@

$(HOME)/rpmbuild/SOURCES:
	$(CMD_PREFIX) rpmdev-setuptree

$(HOME)/rpmbuild/SOURCES/$(ARCHIVE): $(HOME)/rpmbuild $(HOME)/rpmbuild/SOURCES
	$(CMD_PREFIX) spectool -R -g $(SPEC)

rpm: $(HOME)/rpmbuild/SOURCES/$(ARCHIVE)
	$(CMD_PREFIX) rpmbuild -ba $(SPEC)

clean:
	-rm $(ARCHIVE)

# docker targets
.PHONY: docker-image

docker-image:
	$(DOCKER_CMD) build --build-arg=USERID=$(USERID) -t $(IMAGE) .
