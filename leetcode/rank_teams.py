
from collections import defaultdict
from typing import List

class Solution:

    def find_best_team(self, rank_map, rank, teams):
        best_teams = []
        max_position_count = 0
        position_rank_map = rank_map[rank]

        teams = sorted(teams)
        for team in teams:
            if position_rank_map[team] > max_position_count:
                best_teams = [team, ]
                max_position_count = position_rank_map[team]
            if position_rank_map[team] == max_position_count:
                best_teams.append(team)

        if len(best_teams) == 1:
            return best_teams[0]
        elif rank < self.vote_size:
            return self.find_best_team(rank_map, rank + 1, best_teams)
        elif rank >= self.vote_size:
            return teams[0]

    def rankTeams(self, votes: List[str]) -> str:
        self.vote_size = len(votes[0])
        rank_map = {}

        for i in range(1, self.vote_size + 1):
            rank_map[i] = defaultdict(int)

        for vote in votes:
            for rank, team in enumerate(vote, 1):
                rank_map[rank][team] += 1

        best_teams = []
        for rank in range(1, self.vote_size + 1):
            teams_on_rank = rank_map[rank].keys()
            teams_on_rank = [t for t in teams_on_rank if t not in best_teams]
            while teams_on_rank:
                if len(teams_on_rank) == 1:
                    best_teams.append(teams_on_rank[0])
                    break
                elif len(teams_on_rank) > 1:
                    best_one = self.find_best_team(rank_map, 1, teams_on_rank)
                    best_teams.append(best_one)
                    teams_on_rank.remove(best_one)

        return "".join(best_teams)

# votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
votes = ["WXYZ", "XYZW"]
votes = ["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]
ans = Solution().rankTeams(votes)
print(ans)


