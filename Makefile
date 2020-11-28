requirements:
	pip-compile --no-header --no-emit-index-url

dev-requirements:
	pip-compile --no-header --no-emit-index-url dev-requirements.in 

install:
	pip3 install -r requirements.txt -r dev-requirements.txt
    
create-cluster:
	./kind-with-registry.sh

delete-cluster:
	kind delete cluster

e2e:
	pytest -m "e2e"

test:
	pytest -vv

apply-dev-cluster:
	kubectl --context=kind-kind apply -f cluster/echoserver-app.yaml
	kubectl --context=kind-kind apply -f cluster/ingress-minimal.yaml

tear_up: create-cluster apply-dev-cluster

tear_down: delete-cluster
	docker rm -f kind-registry

build_push_run:
	./build_and_push.sh
	kubectl apply -f cluster/ingress-controller.yaml
