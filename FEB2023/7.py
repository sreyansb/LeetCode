#attempt1:
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        number_unique = 0
        max_total = 0
        cur_size = 0
        for index,fruit_type in enumerate(fruits):
            if fruit_type not in window:
                if number_unique < 2:
                    number_unique += 1
                else:
                    highest_last_seen = max(window.values())
                    least_last_seen = min(window.values()) 
                    number_of_same_in_between = highest_last_seen-least_last_seen
                    cur_size = number_of_same_in_between
                    key_to_be_removed = -1
                    for key in window:
                        if window[key] == least_last_seen:
                            key_to_be_removed = key
                            break
                    del window[key_to_be_removed]
            window[fruit_type] = index
            cur_size += 1
            max_total = max(max_total, cur_size)
        return max_total

