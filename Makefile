DST_DIR=~/opt/add_slide
DST_BIN_DIR=$(DST_DIR)/bin
BIN_DIR=~/bin
SRC_SCRIPT=./src/add_slide.py
DST_SCRIPT=$(BIN_DIR)/add_slide

all:
	@echo "If you want to install this script, run 'make install'."

$(DST_DIR):
	mkdir -p $@

$(DST_BIN_DIR):
	mkdir -p $@

$(BIN_DIR):
	mkdir -p $p

install: $(SRC_SCRIPT) $(BIN_DIR) $(DST_DIR) $(DST_BIN_DIR)
	cp -p $< $(DST_BIN_DIR)
	cp -pr ./template $(DST_DIR)/.
	chmod u+x $(DST_BIN_DIR)/${<F}
	ln -s $(DST_BIN_DIR)/${<F} $(DST_SCRIPT)

clean:
ifneq (, $(wildcard $(DST_SCRIPT)))
	rm $(DST_SCRIPT)
endif
ifneq (, $(wildcard $(DST_DIR)))
	rm -r ${DST_DIR}
endif
