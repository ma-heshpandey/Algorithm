class HashTable:

    def __init__(self,size):
        self.size=size          #size of array for using dictionary
        self.hash_list=[None for i in range(self.size)]      #actual array where we will put values

    def get_the_hash_index(self,value):
        sum=0
        for char in value:
            sum+=ord(char)  #gives ASCII value
        hash_value=sum%self.size
        return hash_value

    def __setitem__(self,key,value):
        h=self.get_the_hash_index(key)
        self.hash_list[h]=value

    def __getitem__(self,key):
        h=self.get_the_hash_index(key)
        return self.hash_list[h]


hash1=HashTable(10)
hash1['march 6']=150   # or hash1.add('march 6',150)
print(hash1['march 6'])   # or print(hash1.get('march 6')) use of magical function 


