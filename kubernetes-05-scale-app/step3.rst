To scale down the Service to 1 replica, run again the ``scale``
command:

``kubectl scale deployments/nginx --replicas=1``\ {{execute}}

List the Deployments to check if the change was applied with the
``get deployments`` command:

``kubectl get deployments``\ {{execute}}

The number of replicas decreased to 1. List the number of Pods, with
``get pods``:

``kubectl get pods -o wide``\ {{execute}}

This confirms that 1 Pod was terminated.
