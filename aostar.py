
import copy
import queue

# import the user defined modules
from board import *
from priority import PQ

# search class to search for the best move


class Search:
    def __init__(self,start):
        self.parentTrace = {}
        self.start = start
        self.gamePath = []
        self.movePath = []
        self.numMoves = 0
        self.end = None
            
    def unwindPath(self):
            if self.end:
                target = self.end
            else:
                target = constructTargetBoard(self.start.numRods,self.start.numDisks,self.start.targetRod)
    
            startHash = self.start.hash()
            nextHash = target.hash()
    
            self.gamePath = []
            self.movePath = []
    
            if not startHash == nextHash:
                while(True):
                    self.gamePath.insert(0,constructBoard(nextHash,self.start.numRods,self.start.numDisks,self.start.targetRod))
                    if startHash == nextHash:
                        break
                    else:
                        moves = self.parentTrace[nextHash][1]
                        self.movePath.insert(0,moves)
                        nextHash = self.parentTrace[nextHash][0]
            
            self.numMoves = len(self.movePath)
            
    def printPath(self,verbose = False):
            if verbose:
                counter = 0
                for i in range(len(self.gamePath)):
                    if counter == 0:
                        print("original")
                        print("Heuristic = " + str(self.gamePath[i].heuristic()) + " : Actual Dist = " + str(len(self.gamePath) - counter - 1))
                        self.gamePath[i].printBoard()
                    else:
                        print("Move = " + str(counter) + " : " + str(self.movePath[counter - 1]))
                        print("Heuristic = " + str(self.gamePath[i].heuristic()) + " : Actual Dist = " + str(len(self.gamePath) - counter - 1))
                        self.gamePath[i].printBoard()
                    print("----------------------------------------")
                    counter += 1
            else:
                for i in range(len(self.movePath)):
                    print("Move = " + str(i + 1) + " : " + str(self.movePath[i]))
                    
class AOstarSearch(Search):
    def __init__(self,start):
        super().__init__(start)
        self.end = constructTargetBoard(start.numRods,start.numDisks,start.targetRod)
        self.endHash = self.end.hash()
        self.openSet = PQ()
        self.openSet.update(start)
        self.closedSet = {}
        self.gScore = {start.hash():0}
        self.parentTrace[start.hash()] = {}
        self.search()

    # create a tree and apply AO* search using openset
    def search(self):
        while not self.openSet.isEmpty():
            current = self.openSet.pop()
            chash = current.hash()
            if current.isFinished():
                self.unwindPath()
                return
            successors = current.successor()
            self.closedSet[chash] = True
            for successor in successors:
                shash = successor[0].hash()
                if shash in self.closedSet:
                    continue
                temp_gScore = self.gScore[chash] + 1
                if shash not in self.gScore:
                    self.gScore[shash] = temp_gScore
                elif temp_gScore >= self.gScore[shash]:
                    continue
                else:
                    self.gScore[shash] = temp_gScore
                self.parentTrace[shash] = (chash,successor[1])
                self.openSet.update(successor[0],temp_gScore)   
                
if __name__ == "__main__":
    rods = int(input("Please enter the number of rods: "))
    disks = int(input("Please enter the number of disks: "))
    targetRod = int(input("Please enter the target rod number: "))
    board = towerOfHanoi(rods,disks,targetRod-1)
    AOstarSearch(board).printPath(True)