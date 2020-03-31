PY_FILES=$(wildcard *.py)
ALL_FILES=$(PY_FILES)
VERSION=0.0-1
NAME=random-tools
PACKAGE=random-tools_$(VERSION)

all: package

package: $(ALL_FILES)
	./package.sh $(NAME) $(VERSION)

clean:
	rm -r /tmp/$(PACKAGE)
