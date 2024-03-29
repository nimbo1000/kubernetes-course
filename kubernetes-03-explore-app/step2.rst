Recall that Pods are running in an isolated, private network - so we
need to proxy access to them so we can debug and interact with them. To
do this, we'll use the ``kubectl proxy`` command to run a proxy. Use the command below to run the ``proxy`` in the background:

``kubectl proxy &``\

Now again, we'll get the Pod name and query that pod directly through
the proxy. To get the Pod name and store it in the POD\_NAME environment
variable:

``export POD_NAME=$(kubectl get pods -o go-template --template '\{\{range .items}}\{\{.metadata.name}}\{\{"\n"}}\{\{end}}') && echo Name of the Pod: $POD_NAME``\ 

To see the output of our application, run a ``curl`` request.

``curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/``\ 

The url is the route to the API of the Pod.
