/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {

    var digitSum = function(num) {
        temp = 0
        while (num)  {
            temp += num % 10
            num = Math.floor(num/10)
        }
        return temp
    
    }
    

    let totalElement = 0
    let totalDigit = 0
    for (let num of nums) {
        totalElement += num
        totalDigit += digitSum(num)
    }

    console.log(totalElement)
    console.log(totalDigit)
    


    return Math.abs(totalElement - totalDigit)
   

 
};