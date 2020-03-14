#https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = {
            5: 0,
            10: 0
        }

        for bill in bills:

            if bill == 5:
                cnt[5] += 1

            elif bill == 10:
                cnt[5] -= 1
                cnt[10] += 1

            else:
                if cnt[10] > 0:
                    cnt[10] -= 1
                    cnt[5] -= 1
                else:
                    cnt[5] -= 3

            if cnt[5] < 0:
                return False

        return True
