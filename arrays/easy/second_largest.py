#Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

class solution:
    def __init__(self,arr):
        self.arr = arr
        pass

    def largest(self):
        maximum = float('-inf')
        for i in self.arr:
            if i > maximum:
                maximum = i
        return maximum
    
    def smallest(self):
        minimum = float('inf')
        for i in self.arr:
            if i < minimum:
                minimum = i
        return minimum        



    def second_largest(self):
        largest = self.largest()
        second_lar = float('-inf')
        for i in self.arr:
            if i < largest and i > second_lar:
                second_lar = i
        return second_lar   

    def second_smallest(self):
        smallest = self.smallest()
        second_small = float('inf')
        for i in self.arr:
            if i < second_small and i > smallest:
                second_small = i    
        return second_small         

    def print(self):
        print(f"Second largest element is {self.second_largest()}")
        print(f"Second smallest element is {self.second_smallest()}")

sec = solution([-1,-3,-1.5,0,1,2,2,3,3,4,5,6,7,9, 100000])
sec.print()                    

                

