class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n = len(players)
        m = len(trainers)
        match = 0
        i = j = 0
        while i < n and j < m:
            if players[i] <= trainers[j]:
                match += 1
                i += 1 
            j += 1
        return match