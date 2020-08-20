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
 		clusterInfo = False
		getNodes = False
		if inputCommand == "kubectl cluster-info":
			clusterInfo = True
		if inputCommand == "kubectl get nodes":
			getNodes = True
		if clusterInfo and getNodes:
			return True
