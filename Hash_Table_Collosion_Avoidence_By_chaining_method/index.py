""" 
Two method for collosion avoidence in hash_value
1. Linear probing: It assigns the value at next avilable space
2. Chaining :list or link list is created for connection with same hash_value
"""

class HashTable:

    def __init__(self,size):
        self.size=size          #size of array for using dictionary
        self.hash_list=[[] for i in range(self.size)]      #actual array where we will put values

    def get_the_hash_index(self,value):
        sum=0
        for char in value:
            sum+=ord(char)  #gives ASCII value
        hash_value=sum%self.size
        return hash_value


    def __setitem__(self, key, val):
        h = self.get_the_hash_index(key)
        found = False
        for idx, element in enumerate(self.hash_list[h]):  #iterate through tuples in list
            if len(element)==2 and element[0] == key:
                self.hash_list[h][idx] = (key,val)
                found = True
        if not found:
            self.hash_list[h].append((key,val))


    def __getitem__(self,key):
        h=self.get_the_hash_index(key)
        
        for element in self.hash_list[h]:
            if element[0]==key:
                return element[1]  
        
        #functions return None if return is not executed
        # or raise Exception('Key not found')
            
                
                
    def __delitem__(self,key):
        h=self.get_the_hash_index(key)
        
        for index,element in enumerate(self.hash_list[h]):
            if element[0]==key:
                del self.hash_list[h][index]
        


hash1=HashTable(10)
hash1['march 6']=150   # or hash1.add('march 6',150)
  # or print(hash1.get('march 6')) use of magical function 

hash1['march 17']=250

print(hash1['march 6']) 
print(hash1['march 19'])
del hash1['march 17']
print(hash1.hash_list)




