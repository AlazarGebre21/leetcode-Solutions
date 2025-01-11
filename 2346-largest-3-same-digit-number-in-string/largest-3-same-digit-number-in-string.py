class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""  # To store the largest good integer
        for i in range(len(num) - 2):  # Iterate through the string
            substring = num[i:i+3]  # Extract a substring of length 3
            if substring[0] == substring[1] == substring[2]:  # Check if all characters are the same
                largest = max(largest, substring)  # Update the largest good integer if needed
        return largest
