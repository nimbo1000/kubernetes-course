from onpit import Grader
from os.path import join, exists

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "kubectl create deployment nginx --image=nginx":
			self.firstCommand1 = True
		if inputCommand == "kubectl get deployments":
			self.secondCommand1 = True
		if inputCommand == """export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\\n"}}{{end}}') && echo Name of the Pod: $POD_NAME""":
			self.thirdCommand1 = True
		if inputCommand == "kubectl scale deployments/nginx --replicas=2":
			self.fourthCommand1 = True
		if inputCommand == "kubectl get pods -o wide":
			self.fifthCommand1 = True
		if inputCommand == "kubectl describe deployments/nginx":
			self.sixthCommand1 = True
		if hasattr(self, 'firstCommand1') and hasattr(self, 'secondCommand1') and hasattr(self, 'thirdCommand1') and hasattr(self, 'fourthCommand1') and hasattr(self, 'fifthCommand1') and hasattr(self, 'sixthCommand1') and self.firstCommand1 and self.secondCommand1 and self.thirdCommand1 and self.fourthCommand1 and self.fifthCommand1 and self.sixthCommand1:
			return True

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		if inputCommand == """kubectl expose deployment/nginx --type="NodePort" --port 80""":
			self.firstCommand2 = True
		if inputCommand == "kubectl describe services/nginx":
			self.secondCommand2 = True
		if inputCommand == "export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{;(index .spec.ports 0).nodePort}}') echo NODE_PORT=$NODE_PORT":
			self.thirdCommand2 = True
		if inputCommand == "kubectl exec -ti $POD_NAME bash":
			self.fourthCommand2 = True
		if inputCommand == "curl 127.0.0.1:$NODE_PORT":
			self.fifthCommand2 = True
		if hasattr(self, 'firstCommand2') and hasattr(self, 'secondCommand2') and hasattr(self, 'thirdCommand2') and hasattr(self, 'fourthCommand2') and hasattr(self, 'fifthCommand2') and self.firstCommand2 and self.secondCommand2 and self.thirdCommand2 and self.fourthCommand2 and self.fifthCommand2:
			return True

	@Grader.addStep(name='step3')
	def step3(self, workingDir, inputCommand):
		if inputCommand == "kubectl scale deployments/nginx --replicas=1":
			self.firstCommand3 = True
		if inputCommand == "kubectl get deployments":
			self.secondCommand3 = True
		if inputCommand == "kubectl get pods -o wide":
			self.thirdCommand3 = True
		if hasattr(self, 'firstCommand3') and hasattr(self, 'secondCommand3') and hasattr(self, 'thirdCommand3') and self.firstCommand3 and self.secondCommand3 and self.thirdCommand3:
			return True
