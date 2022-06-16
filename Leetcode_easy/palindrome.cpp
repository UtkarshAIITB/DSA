#include<iostream>
#include <vector>
using namespace std;
using std::vector;

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || (x%10 == 0 && x!=0)){
            return false;
        }
        int invert = 0;
        while(x > invert){
            invert = invert*10 + x%10;
            x/=10;
        }
        return x == invert || x == invert/10;
    }
};