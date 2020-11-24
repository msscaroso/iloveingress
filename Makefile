requirements:
	pip-compile --no-header --no-emit-index-url

    

dev-requirements:
	pip-compile --no-header --no-emit-index-url dev-requirements.in 

install:
	pip3 install -r requirements.txt -r dev-requirements.txt
