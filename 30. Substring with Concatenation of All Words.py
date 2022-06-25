from collections import Counter


class Solution_1:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        words_len = len(words)
        sub_len = word_len * words_len
        counter = Counter(words)
        result = []
        for i in range(len(s) - sub_len + 1):
            if self.check(s, i, counter, words_len, word_len):
                result.append(i)
        return result
            
            
    def check(self, s: str, start: int, counter: dict, words_len: int, word_len: int) -> bool:
        counter_copy = counter.copy()
        for i in range(start, start + (word_len * words_len), word_len):
            word = s[i:i + word_len]
            if counter_copy[word] > 0:
                counter_copy[word] -= 1
            else:
                return False
        return True
    

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        words_len = len(words)
        sub_len = word_len * words_len
        counter = Counter(words)
        result = []
        for i in range(word_len):
            result.extend(self.check(counter, s, i, sub_len, word_len))
        return result
            
            
    def check(self, counter: dict, s: str, shift: int, sub_len: int, word_len: int) -> bool:
        counter_copy = counter.copy()
        result = []
        for i in range(shift, len(s) - word_len + 1, word_len):
            # если продвинулсиь уже достаточно далеко, чтобы удалить первое слово из начала, то делаем это
            if i - sub_len >= 0:
                rem_word = s[i - sub_len :i - sub_len + word_len]
                counter_copy[rem_word] += 1
                if counter_copy[rem_word] == 0:
                    counter_copy.pop(rem_word)
            add_word = s[i:i + word_len]
            counter_copy[add_word] -= 1
            if counter_copy[add_word] == 0:
                counter_copy.pop(add_word)
            if not counter_copy:
                result.append(i - sub_len + word_len)
        return result

        

print(Solution().findSubstring(
    "barfoothefoobarman",
    ["foo","bar"],
))
