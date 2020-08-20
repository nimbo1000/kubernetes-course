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
		this.clusterInfo = False
		this.getNodes = False
		if inputCommand == "kubectl cluster-info":
			this.clusterInfo = True
		if inputCommand == "kubectl get nodes":
			this.getNodes = True
		if this.clusterInfo and this.getNodes:
			return True
