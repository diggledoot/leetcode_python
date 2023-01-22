class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        result_string = ""
        # Result
        max_length = 0

        # Return zero or 1 if string is empty or only 1 length
        if len(string) == 0 or len(string) == 1:
            return len(string)

        for character in string:
            # If string already contains the character
            # Then substring after repeating character
            if character in result_string:
                result_string = result_string[result_string.index(character)+1:]

            result_string = result_string + character

            if max_length < len(result_string):
                max_length = len(result_string)

        return max_length
