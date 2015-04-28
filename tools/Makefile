all: ../turtle/manifest-ldpatch.ttl
	python gen-variants.py
	python gen-syntax-manifest.py
	python check.py
	python gen-reports-README.py > ../reports/README.rst

../turtle/manifest-ldpatch.ttl: ../turtle/manifest.ttl
	python tr-turtle-manifest.py


clean-variants:
	rm -f ../s_*.v.ldpatch

clean-turtle:
	@if [ ! -e ../turtle/manifest.ttl ]; \
	then echo "NOT cleaning, as you do not have the original files..."; \
	else rm -f ../turtle/manifest-ldpatch.ttl ../turtle/*.ldpatch ../turtle/*+scd.nt ; \
	fi

.PHONY: all clean-variants clean-turtle
