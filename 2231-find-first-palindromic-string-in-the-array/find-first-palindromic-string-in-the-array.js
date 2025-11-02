/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    
    for (let word of words) {

        temp = [...word].reverse().join('')

        if (temp == word){
            return temp
        }

    }

    return ""
    
};