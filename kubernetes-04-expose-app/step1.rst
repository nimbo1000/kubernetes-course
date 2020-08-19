Let’s verify that our application is running. We’ll use the
``kubectl get`` command and look for existing Pods:

``kubectl get pods``

Next let’s list the current Services from our cluster:

``kubectl get services``

We have a Service called kubernetes that is created by default when
the cluster starts. To create a new service and expose it to
external traffic we’ll use the expose command with NodePort as parameter.

``kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080``

Let’s run again the ``get services`` command:

``kubectl get services``

We have now a running Service called kubernetes-bootcamp. Here we see
that the Service received a unique cluster-IP, an internal port and an
external-IP (the IP of the Node).

To find out what port was opened externally (by the NodePort option)
we’ll run the ``describe service`` command:

``kubectl describe services/kubernetes-bootcamp``

Create an environment variable called NODE\_PORT that has the value of
the Node port assigned:

``export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='&#123;&#123;(index .spec.ports 0).nodePort&#125;&#125;') echo NODE_PORT=$NODE_PORT``\ {{execute}}

Now we can test that the app is exposed outside of the cluster using
``curl``, the IP of the Node and the externally exposed port:

``curl $(minikube ip):$NODE_PORT``

And we get a response from the server. The Service is exposed.
