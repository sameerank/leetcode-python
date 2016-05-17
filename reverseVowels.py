class Solution(object):
    def reverseVowels(self, s):
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_stack = []
        s_copy = []
        for letter in s:
            s_copy.append(letter)
            if letter in vowel_set:
                vowel_stack.append(letter)

        for index, letter in enumerate(s_copy):
            if letter in vowel_set:
                s_copy[index] = vowel_stack.pop()

        return "".join(s_copy)
        """
        :type s: str
        :rtype: str
        """
