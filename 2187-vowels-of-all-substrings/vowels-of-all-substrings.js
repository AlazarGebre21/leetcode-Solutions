/**
 * @param {string} word
 * @return {number}
 */
var countVowels = function(word) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u'])
    let ans = 0


    for (const [index, letter] of [...word].entries()) {
        if (vowels.has(letter)) {
            ans += ((word.length - index) * (index + 1))

        }

    }

    return ans
};