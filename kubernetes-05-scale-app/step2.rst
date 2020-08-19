Let’s check that the Service is load-balancing the traffic. First, expose the service as in previous lab:

``kubectl expose deployment/nginx --type="NodePort" --port 80``

To find out the exposed IP and Port we can use:

``kubectl describe services/nginx``\ {{execute}}

Create an environment variable called NODE\_PORT that has a value as the
Node port:

``export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='\{\{;(index .spec.ports 0).nodePort}}') echo NODE_PORT=$NODE_PORT``\ {{execute}}

We can get terminal access to the first replica of the deployment:

``kubectl exec -ti $POD_NAME bash``

Inside the container we can change the content of the server's response:

``echo "<html>Welcome to the first nginx container</html>" > /usr/share/nginx/html/index.html``

We can use ``exit`` to get back to the node terminal.

Next, we’ll do a ``curl`` to the exposed IP and port. Execute the
command multiple times:

``curl 127.0.0.1:$NODE_PORT``\ {{execute}}

We hit a different Pod with every request. This demonstrates that the
load-balancing is working.
