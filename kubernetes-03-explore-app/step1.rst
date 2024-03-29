Let’s deploy our application again:

``kubectl run nginx --image=nginx --port=80``

To verify that the application is running, we’ll use the ``kubectl get`` command and look for existing
Pods:

``kubectl get pods``\ {{execute}}

If no pods are running, list the Pods again.

Next, to view what containers are inside that Pod and what images are
used to build those containers we run the ``describe pods`` command:

``kubectl describe pods``\ {{execute}}

We see here details about the Pod’s container: IP address, the ports
used and a list of events related to the lifecycle of the Pod.

The output of the describe command is extensive and covers some concepts
that we didn’t explain yet, but don’t worry, they will become familiar
by the end of this bootcamp.

*Note: the describe command can be used to get detailed information
about most of the kubernetes primitives: node, pods, deployments. The
describe output is designed to be human readable, not to be scripted
against.*
