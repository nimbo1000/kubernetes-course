while ! test -f "/etc/rancher/k3s/k3s.yaml"; do
	  sleep 2
	    echo "Still waiting"
    done
    chmod +r /etc/rancher/k3s/k3s.yaml
    KUBECONFIG="~/.kube/config:/etc/rancher/k3s/k3s.yaml"

