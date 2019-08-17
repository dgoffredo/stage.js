.PHONY: all
all: dist/stage.web.js dist/stage.cordova.js

SOURCES=$(shell python bin/sources.py)

dist/stage.web.js: $(SOURCES)
	browserify platform/web --standalone Stage > dist/stage.web.js

dist/stage.cordova.js: $(SOURCES)
	browserify platform/cordova --standalone Stage > dist/stage.cordova.js
