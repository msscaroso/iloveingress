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

apply-dev-cluster:
	kubectl --context=kind-kind apply -f cluster/nginx.yaml
	kubectl --context=kind-kind apply -f cluster/ingress-minimal.yaml

tear_up: create-cluster apply-dev-cluster

tear_down: delete-cluster
