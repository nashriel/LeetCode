from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dfs(players):
            round_size = len(players)
            for i in range(round_size // 2):
                if (players[i] == firstPlayer and players[-1 - i] == secondPlayer) or \
                   (players[i] == secondPlayer and players[-1 - i] == firstPlayer):
                    return (1, 1)
            
            min_round, max_round = float('inf'), 0

            # Build all valid outcomes (either player can win non-FP/SP matches)
            def get_next_round(players):
                pairings = []
                mid = None
                n = len(players)
                for i in range(n // 2):
                    a, b = players[i], players[n - 1 - i]
                    if {a, b} == {firstPlayer, secondPlayer}:
                        continue
                    elif a == firstPlayer or a == secondPlayer:
                        pairings.append([a])
                    elif b == firstPlayer or b == secondPlayer:
                        pairings.append([b])
                    else:
                        pairings.append([a, b])
                if n % 2 == 1:
                    mid = [players[n // 2]]
                return pairings, mid

            from itertools import product
            pairings, mid = get_next_round(players)
            for prod in product(*pairings):
                nxt = list(prod)
                if mid:
                    nxt += mid
                nxt.sort()
                rmin, rmax = dfs(tuple(nxt))
                min_round = min(min_round, rmin + 1)
                max_round = max(max_round, rmax + 1)

            return (min_round, max_round)

        players = tuple(range(1, n + 1))
        return list(dfs(players))
