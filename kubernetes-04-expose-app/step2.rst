We can use the label to query our list of Pods. We’ll use the
``kubectl get pods`` command with -l as a parameter, followed by the
label values:

``kubectl get pods -l run=nginx``\ {{execute}}

You can do the same to list the existing services:

``kubectl get services -l run=nginx``\ {{execute}}

Get the name of the Pod and store it in the POD\_NAME environment
variable:

``export POD_NAME=$(kubectl get pods -o go-template --template '\{\{range .items}}\{\{.metadata.name}}\{\{"\n"}}\{\{end}}') && echo Name of the Pod: $POD_NAME``\ {{execute}}

To apply a new label we use the label command followed by the object
type, object name and the new label:

``kubectl label pod $POD_NAME app=v1``\ {{execute}}

This will apply a new label to our Pod (we pinned the application
version to the Pod), and we can check it with the describe pod command:

``kubectl describe pods $POD_NAME``\ {{execute}}

We see here that the label is attached now to our Pod. And we can query
now the list of pods using the new label:

``kubectl get pods -l app=v1``\ {{execute}}

And we see the Pod.
