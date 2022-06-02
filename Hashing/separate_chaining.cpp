// ways to deal with collisions in hashing = separate chaining and open addressing
// separate chaining uses linked lists

#include <iostream>
#include <list>  //linked list
#include <cstring>  //key value  = string
using namespace std;


//hastable to implement 905, jim

class HashTable{
	private:
		static const int hashGroups = 10;
		// array that is going to store list and that will contain pairs
		list<pair<int, string>> table[hashGroups]; //List 1, Index 0, List 2, Index 1

	public:
		bool isEmpty() const;
		int hashFunction(int key);
		void insertItem(int key, string value);
		void removeItem(int key);
		string searchTable(int key);
		void printTable();
};

bool HashTable::isEmpty() const{
	int sum{};
	for (int i{}; i<hashGroups; i++){
		sum += table[i].size();
	}

	if(!sum){
		return true;
	}
	return false;
}

int HashTable::hashFunction(int key){
	// return a value b/w 0 and 9
	return key % hashGroups; //Key:905 will return 5
}

void HashTable::insertItem(int key, string value){
	int hashValue = hashFunction(key);
	auto& cell = table[hashValue];
	auto bItr = begin(cell);
	bool keyExists = false;
}