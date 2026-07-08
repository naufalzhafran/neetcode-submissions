class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)

        for item in strs:
            sorted_string = "".join(sorted(item))
            result_dict[sorted_string].append(item)

        return list(result_dict.values())