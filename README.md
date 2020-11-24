# I Love Ingress

Creating a ingress just for fun

### Running e2e tests

1) [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/) cluster with 1 contro-plane and 2 worker nodes
2) [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) with 3 replicas running nginx http server
3) [Service](https://kubernetes.io/docs/concepts/services-networking/service/) exposing the nginx deployment

```shell script
make tear_up
``` 

### Requirements 

- python
- pip-tools
- kind
- kubectl
