# I Love Ingress

Creating an ingress controller just for fun


### Requirements 

- kind
- docker
- kubectl

### Running

First, setup the kind cluster

```shell script
make tear_up
```

Then build, push and run the ingress controller inside the
cluster

```shell script
make build_push_run
```

Now you can access the ingress-controller through its service
`iloveingress-nginx` inside a node

```shell script
docker exec -it <node_id> bash
curl <svc_cluster_ip>
```

