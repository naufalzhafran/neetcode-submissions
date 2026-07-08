class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}

        for item in strs:
            sorted_string = "".join(sorted(item))
            current = result_dict.get(sorted_string, [])

            result_dict[sorted_string] = current
            result_dict[sorted_string].append(item)

        result = []

        for value in result_dict.values():
            result.append(value)

        return result