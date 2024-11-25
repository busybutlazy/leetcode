from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        turn_left={(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}        
        turn_right={(-1,0):(0,1),(0,-1):(-1,0),(1,0):(0,-1),(0,1):(1,0)}
        direction=(0,1)
        location=[0,0]
        obstacles_map={}
        longest_dis=0

        for obst in obstacles:
            if obst[0] not in obstacles_map:
                obstacles_map.update({obst[0]:{obst[1]:True}})
            else:
                obstacles_map[obst[0]].update({obst[1]:True})

        for com in commands:
            if com == -2:
                direction = turn_left[direction]
            elif com == -1:
                direction = turn_right[direction]
            elif com >=1 and com <=9:
                print("com=",com,"   pre_location=",location)
                while com >=1:
                    location[0]+=direction[0]
                    location[1]+=direction[1]
                    if location[0] in obstacles_map and location[1] in obstacles_map[location[0]]:
                        location[0]-=direction[0]
                        location[1]-=direction[1]
                        break
                    com-=1
                print("location=",location)
                if longest_dis<location[0]**2+location[1]**2:
                    longest_dis=location[0]**2+location[1]**2

        return longest_dis


if __name__=="__main__":
    solution = Solution()
    commands=[6,-1,-1,6]
    obstacles=[]
    print(solution.robotSim(commands,obstacles))