// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

#include<iostream>
#include <vector>
using namespace std;
using std::vector;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i<nums.size(); i++){
            for (int j=i+1; j<nums.size(); j++){
                if(nums[i]+nums[j] == target){
                    return (vector<int>(i,j));
                }
            }
        }
        return vector<int>();
    }
};

//  This solution is of order O(n^2)

// Approach2: Two pass hash table
// To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array. 
// If the complement exists, we need to get its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.
// We can reduce the lookup time from O(n)O(n) to O(1)O(1) by trading space for speed. A hash table is well suited for this purpose because it supports 
// fast lookup in near constant time. I say "near" because if a collision occurred, a lookup could degenerate to O(n)O(n) time.
// However, lookup in a hash table should be amortized O(1)O(1) time as long as the hash function was chosen carefully. 


// A simple implementation uses two iterations. In the first iteration, we add each element's value as a key and its index as a value to the hash table. 
// Then, in the second iteration, we check if each element's complement (target - nums[i]) exists in the hash table. If it does exist, 
// we return current element's index and its complement's index. Beware that the complement must not be nums[i] itself!



// class Solution {
//     public int[] twoSum(int[] nums, int target) {
//         Map<Integer, Integer> map = new HashMap<>();
//         for (int i = 0; i < nums.length; i++) {
//             map.put(nums[i], i);
//         }
//         for (int i = 0; i < nums.length; i++) {
//             int complement = target - nums[i];
//             if (map.containsKey(complement) && map.get(complement) != i) {
//                 return new int[] { i, map.get(complement) };
//             }
//         }
//         // In case there is no solution, we'll just return null
//         return null;
//     }
// }




