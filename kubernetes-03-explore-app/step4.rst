We can execute commands directly on the container once the Pod is up and
running. For this, we use the ``exec`` command and use the name of the
Pod as a parameter. Let’s list the environment variables:

``kubectl exec $POD_NAME env``

Again, worth mentioning that the name of the container itself can be
omitted since we only have a single container in the Pod.

Next let’s start a bash session in the Pod’s container:

``kubectl exec -ti $POD_NAME bash``

We have now an open console on the container where our web
application is running. 
You can check that by running a curl command:

``curl localhost:80``

*Note: here we used localhost because we executed the command inside the container*

To close your container connection type ``exit``.
