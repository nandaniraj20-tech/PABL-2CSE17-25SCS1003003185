def two_sum(nums, target):
   
    seen_numbers = {}
    
    for i, num in enumerate(nums):
       
        partner = target - num
        
        
        if partner in seen_numbers:
            
            return [seen_numbers[partner], i]
        
        
        seen_numbers[num] = i


nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))  
