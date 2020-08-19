Pods that are running inside Kubernetes are running on a private,
isolated network. By default they are visible from other pods and
services within the same kubernetes cluster, but not outside that
network. When we use ``kubectl``, we're interacting through an API
endpoint to communicate with our application.

We will cover other options on how to expose your application outside
the kubernetes cluster in Module 4.

The ``kubectl`` command can create a proxy that will forward
communications into the cluster-wide, private network. The proxy can be
terminated by pressing control-C and won't show any output while its
running.

We will run the proxy on the background.

``kubectl proxy &``

We now have a connection between our host (the online terminal) and the
Kubernetes cluster. The proxy enables direct access to the API from
these terminals.

You can see all those APIs hosted through the proxy endpoint, now
available at through http://localhost:8001. For example, we can query
the version directly through the API using the ``curl`` command:

``curl http://localhost:8001/version``

The API server will automatically create an endpoint for each pod, based
on the pod name, that is also accessible through the proxy.

First we need to get the Pod name, and we'll store in the environment
variable POD\_NAME:

``export POD_NAME=$(kubectl get pods -o go-template --template '\{\{range .items}}\{\{.metadata.name}}\{\{"\n"}}\{\{end}}') && echo Name of the Pod: $POD_NAME``
Now we can make an HTTP request to the application running in that pod:

``curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/``
The url is the route to the API of the Pod.

