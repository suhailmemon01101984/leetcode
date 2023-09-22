class solution():
    def __init__(self):
        print("in init of class: solution")

    def twosum(self,nums,target):
        array_of_ints=nums
        sum_target=target
        output_indices=[0,0]
        break_ind=0
        print(f"here is the array of integers: {array_of_ints}")
        print(f"here is the sum target: {sum_target}")
        for i in range(len(array_of_ints)):
            for j in range(i+1,len(array_of_ints)):
                if(break_ind==1):
                    break
                if(array_of_ints[i]+array_of_ints[j]==sum_target):
                    break_ind=1
                    print(f"{array_of_ints[i]},{array_of_ints[j]}")
                    output_indices[0]=i
                    output_indices[1]=j
                    print(output_indices)
            if(break_ind==1):
                break
        if(output_indices==[0,0]):
            print("there are no two numbers in this array that equal target")






nums=[3,3]
target=6
s=solution()
s.twosum(nums,target)