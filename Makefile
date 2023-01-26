DST_DIR=~/opt/add_slide
BIN_DIR=~/bin

install: ./src/add_slide.py
	mkdir -p ${DST_DIR}
	mkdir -p ${DST_DIR}/bin
	mkdir -p ${BIN_DIR}
	cp -p $< ${DST_DIR}/bin
	cp -pr ./template ${DST_DIR}/.
	chmod u+x ${DST_DIR}/bin/${<F}
	ln -s ${DST_DIR}/bin/${<F} ${BIN_DIR}/${<F}

clean:
	rm ${BIN_DIR}/add_slide.py
	rm -r ${DST_DIR}