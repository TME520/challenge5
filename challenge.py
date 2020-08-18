# Python 3 code to find Maximum difference 
# between two elements such that larger  
# element appears after the smaller number 
  
# The function assumes that there are at  
# least two elements in array. The function  
# returns a negative value if the array is 
# sorted in decreasing order. Returns 0  
# if elements are equal 
def maxDiff(arr, arr_size): 
    max_diff = arr[1] - arr[0] 
      
    for i in range( 0, arr_size ): 
        for j in range( i+1, arr_size ): 
            if(arr[j] - arr[i] > max_diff):  
                max_diff = arr[j] - arr[i] 
      
    return max_diff 
      
# Enter a sample of yesterday's stock market prices here
# Step: 1 minute (lol)
# stock_prices_yesterday = [55, 55, 56, 57, 57, 57, 57, 62, 63, 64, 79, 80]
# stock_prices_yesterday = [1, 2, 90, 10, 110]
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
size = len(stock_prices_yesterday) 
print (f'Best profit from 1 purchase and 1 sale of 1 Latitude Financial stock yesterday: {maxDiff(stock_prices_yesterday, size)}$')
