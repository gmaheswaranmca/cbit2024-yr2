from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0            
        queue = deque([  (beginWord,1) ])
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for I in range(len(word)): #each word letter index
                for ch in 'abcdefghijklmnopqrstuvwxyz': #character is replaced to word 
                    new_word = word[:I] + ch + word[I+1:]
                    if new_word in wordSet:
                        queue.append( (new_word, level + 1) )
                        wordSet.remove(new_word)
        return 0
    
'''
    1. if endWord not in wordList, return 0
    2. bfs with [beginWord + level=1 -> queue]
            process queue iteratively:
                word, level = remove from queue 
                if the word is the endWord:
                    return the level 
                change the word's every letter from one of lower alpha:
                    check the new word is in wordSet:
                        if so:
                            add new word to the queue with level + 1
                            remove from the word set
    3. if words of queue are processed, 
        we say that endWord we cannot transform or achieve ie return 0 
'''    