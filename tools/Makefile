all: ../turtle/manifest-ldpatch.ttl
	python gen-variants.py
	python gen-syntax-manifest.py
	python check.py

../turtle/manifest-ldpatch.ttl: ../turtle/manifest.ttl
	python tr-turtle-manifest.py


clean-variants:
	rm -f ../s_*.v.ldpatch

clean-turtle:
	@if [ ! -e ../turtle/manifest.ttl ]; \
	then echo "NOT cleaning, as you do not have the original files..."; \
	else rm -f ../turtle/manifest-ldpatch.ttl ../turtle/*.ldpatch ../turtle/*+scd.nt ; \
	fi

impl-report:
	python gen-impl-report.py > ../pages/impl-report.html
	@echo /!\ Still need to push gh-pages

.PHONY: all clean-variants clean-turtle impl-report
