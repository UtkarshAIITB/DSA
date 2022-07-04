# link : https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total_tank, curr_tank = 0,0
        starting_station = 0
        
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                starting_position = i+1
                curr_tank = 0
        return starting_station if total_tank >=0 else -1

# interesting approach look at the solution at link