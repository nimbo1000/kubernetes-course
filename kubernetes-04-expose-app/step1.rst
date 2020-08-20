Let’s deploy our application again:

``kubectl run nginx --image=nginx --port=80``

To verify that the application is running, we’ll use the ``kubectl get`` command and look for existing
Pods:

``kubectl get pods``

Next let’s list the current Services from our cluster:

``kubectl get services``

We have a Service called kubernetes that is created by default when
the cluster starts. To create a new service and expose it to
external traffic we’ll use the expose command with NodePort as parameter.

``kubectl expose pod/nginx --type="NodePort" --port 80``

Let’s run again the ``get services`` command:

``kubectl get services``

We have now a running Service called kubernetes-bootcamp. Here we see
that the Service received a unique cluster-IP, an internal port and an
external-IP (the IP of the Node).

To find out what port was opened externally (by the NodePort option)
we’ll run the ``describe service`` command:

``kubectl describe services/nginx``

Create an environment variable called NODE\_PORT that has the value of
the Node port assigned:

``export NODE_PORT=$(kubectl get services/nginx -o go-template='\{\{(index .spec.ports 0).nodePort}}') && echo NODE_PORT=$NODE_PORT``\ {{execute}}
 
Now we can test that the app is exposed outside of the cluster using
``curl``, the IP of the Node and the externally exposed port. From within the node we can also use the localhost IP.

``curl 127.0.0.1:$NODE_PORT``

And we get a response from the server. The Service is exposed.
