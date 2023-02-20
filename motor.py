import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        print(self.jointName)
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        if (self.jointName == b'Torso_BackLeg'):
            self.frequency = c.backLegFrequency/2
        else:
            self.frequency = c.backLegFrequency
        self.amplitude = c.backLegAmplitude
        self.offset = c.backLegPhaseOffset

        self.radianValues = np.linspace(0, 2 * np.pi, num = c.steps)
        self.motorValues = self.amplitude * np.sin(self.frequency * self.radianValues + self.offset)

    def Set_Value(self, robot, time):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[time],
            maxForce = c.motorMaxForce)
            
    def Save_Value(self):
        targetAnglesData = open("data/" + self.jointName + ".npy", "wb")
        np.save(targetAnglesData, self.motorValues)
        targetAnglesData.close()