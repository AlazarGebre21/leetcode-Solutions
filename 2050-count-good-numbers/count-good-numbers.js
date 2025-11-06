/**
 * @param {number} n
 * @return {number}
 */
var countGoodNumbers = function(n) {
    
    const modulo = 1000000007n; 
    function logPower(base, exp) {
        
        let res = 1n;                 
        base = BigInt(base);          
        exp = BigInt(exp);            

       
        while (exp > 0n) {            
            if (exp % 2n === 1n) {   
                res = (res * base) % modulo; 
            }

           
            base = (base * base) % modulo;  

            
            exp = exp / 2n;           
        }
        return res;
    }

    
    const N = BigInt(n);
    let even_place;
    let odd_place;

    if (n % 2 === 0) {
        
        even_place = N / 2n;        
        odd_place = N / 2n;         
    }
    else {
    
        even_place = (N + 1n) / 2n; 
        odd_place = N / 2n;         
    }

    let a = logPower(5n, even_place); 
    let b = logPower(4n, odd_place);   

    
    return Number((a * b) % modulo);   
};
