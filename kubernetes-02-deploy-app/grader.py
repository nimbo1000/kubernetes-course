from onpit import Grader
from os.path import join, exists

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "kubectl version":
			self.firstCommand1 = True
		if inputCommand == "kubectl get nodes":
			self.secondCommand1 = True
		if hasattr(self, 'firstCommand1') and hasattr(self, 'secondCommand1') and self.firstCommand1 and self.secondCommand1:
			return True

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		if inputCommand == "kubectl run nginx --image=nginx --port=80":
			self.firstCommand2 = True
		if inputCommand == "kubectl get pods":
			self.secondCommand2 = True
		if hasattr(self, 'firstCommand2') and hasattr(self, 'secondCommand2') and self.firstCommand2 and self.secondCommand2:
			return True

	@Grader.addStep(name='step3')
	def step3(self, workingDir, inputCommand):
		if inputCommand == "kubectl proxy &":
			self.firstCommand3 = True
		if inputCommand == "curl http://localhost:8001/version":
			self.secondCommand3 = True
		if inputCommand == """export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\\n"}}{{end}}') && echo Name of the Pod: $POD_NAME""":
			self.thirdCommand3 = True
		if inputCommand == "curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/":
			self.fourthCommand3 = True
		if hasattr(self, 'firstCommand3') and hasattr(self, 'secondCommand3') and hasattr(self, 'thirdCommand3') and hasattr(self, 'fourthCommand3') and self.firstCommand3 and self.secondCommand3 and self.thirdCommand3 and self.fourthCommand3:
			return True
