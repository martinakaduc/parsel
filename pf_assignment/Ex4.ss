maximizeHappiestScore(input): takes a string, rearranges the string's characters to get the highest "Happiest score" and prints the result to the screen. You have the right to transpose all characters in the string. A permutation would be equivalent to an array of "Happiness scores". The "Happiness score" in this sentence is calculated as the sum of the ASCII codes of adjacent vowels (a, e, i, o, u, A, E, I, O, U) (vowel clusters). For example, "aebcdef" will be equivalent to a two-element array of "Happiness scores" corresponding to "ae" and "e". "Happiness score" can be "Happy number" or not. "Happy number" is a prime number and the sum of its digits is a power of base 2. "Happiest score" must be a "Happy number" and have the greatest sum of digits. If there is more than one "Happy number" with the largest sum of digits, the "Happiest number" will be the largest number. For each permutation of the string there will be a corresponding "Happiest score". You need to find the largest "Happiest score" and the vowel cluster corresponding to this number across all permutations of the string. If there are no vowels in the input string, the largest "Happiest score" is 0. In case there is more than one "Happiest score" with the same value, the vowel cluster has a shorter length and has more vowels (For example: "aia" has 2 vowels, 'a' and 'i') will prioritized. In the case of the same "Happiest score", the same length and number of vowels in the vowel cluster, the different first character of the vowel cluster with the larger ASCII code will be chosen. 
"i love you" -> "Happiest String: e\nHappiest Score: 101 (Happy)"
"LLL IiI EeE oAo ooo" -> "Happiest String: IIeiooooo\nHappiest Score: 907 (Happy)"
    permute(input): takes a string, returns a list of all permutations of the string.
    "abc" -> ["abc", "acb", "bac", "bca", "cab", "cba"]
    calculateLargestHappiestScore(input): take a list of permutations of the string, returns the largest "Happiest score" and the corresponding vowel cluster.
    ["abc", "acb", "bac", "bca", "cab", "cba"] -> {"a": 97}
    ["aeiou"] -> {"aeiou": 545}
        getListOfVowelClusters(input): takes a string, returns a list of all vowel clusters in the string.
        "abcde" -> ["a", "e"]
        "aeiou" -> ["aeiou"]
        calculateHappiestScore(input): takes a list of vowel clusters, returns the "Happiest score" and the corresponding vowel cluster. "Happiest score" must be a "Happy number" and have the greatest sum of digits. If there is more than one "Happy number" with the largest sum of digits, the "Happiest number" will be the largest number.
        ["a", "e"] -> {"a": 97}
        ["aeiou"] -> {"aeiou": 545}
            computeHappinessScore(input): takes a list of strings, returns the dictionary whose each elements is the sum of the ASCII codes of the characters in a string. "Happiness score" can be "Happy number" or not.
            ["a", "e"] -> {"a": 97, "e": 101}
            ["aeiou"] -> {"aeiou": 545}
            findHappyNumber(input): takes a list of integers, returns the list of "Happy number". "Happy number" is a prime number and the sum of its digits is a power of base 2. 
            [97, 101] -> [101]
            [545] -> []
                isPrime(input): takes an integer, returns True if the number is a prime number, False otherwise.
                101 -> True
                545 -> False
                isSumPowerOfTwo(input): takes an integer, returns True if the sum of the digits of the number is a power of base 2, False otherwise.
                101 -> True
                545 -> False