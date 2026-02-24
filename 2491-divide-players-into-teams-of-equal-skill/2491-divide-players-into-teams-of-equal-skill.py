class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill_sum = sum(skill)
        teams = len(skill) / 2
        team_skill = skill_sum / teams

        chemistry = 0
        skill.sort()

        p1 = 0
        p2 = len(skill) - 1

        while p1 < p2:
            if skill[p1] + skill[p2] != team_skill:
                return -1
            chemistry += skill[p1] * skill[p2]
            p2 -= 1
            p1 += 1
        return chemistry

        