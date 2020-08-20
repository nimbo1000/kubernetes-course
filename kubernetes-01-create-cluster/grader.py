#This is a template for the grader

from onpit import Grader
from os.path import join, exists

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "kubectl version":
			return True

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		if inputCommand == "kubectl cluster-info":
			self.clusterInfo = True
			print("ci true")
		if inputCommand == "kubectl get nodes":
			self.getNodes = True
			print("gn true")
		if hasattr(self, 'clusterInfo') and hasattr(self, 'getNodes') and self.clusterInfo and self.getNodes:
			return True
