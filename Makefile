.PHONY: dist

dist:
	-rm -r dist
	-rm -r build
	python3 setup.py sdist
	python3 setup.py bdist_wheel

fuck:
	echo 'fuck'
