To delete Services you can use the ``delete service`` command. Labels
can be used also here:

``kubectl delete service -l run=nginx``\ {{execute}}

Confirm that the service is gone:

``kubectl get services``\ {{execute}}

This confirms that our Service was removed. To confirm that route is not
exposed anymore you can ``curl`` the previously exposed IP and port:

``curl 127.0.0.1:$NODE_PORT``\ {{execute}}

This proves that the app is not reachable anymore from outside of the
cluster. You can confirm that the app is still running with a curl
inside the pod:

``kubectl exec -ti $POD_NAME curl localhost:80``\ {{execute}}

We see here that the application is up.
