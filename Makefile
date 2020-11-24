requirements:
	pip-compile --no-header --no-emit-index-url

    

dev-requirements:
	pip-compile --no-header --no-emit-index-url dev-requirements.in 

install:
	pip3 install -r requirements.txt -r dev-requirements.txt
    
create-cluster:
	kind create cluster --config=kind-config.yaml

delete-cluster:
	kind delete cluster

e2e:
	pytest -m "e2e"

test:
	pytest -m "not e2e"

