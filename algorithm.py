import random
import matplotlib.pyplot as plt
import networkx as nx

class Team:
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed


def pair_teams(teams):
    bracket = []
    for i in range(0, len(teams), 2):
        if i + 1 < len(teams):
            bracket.append((teams[i], teams[i + 1]))
        else:
            bracket.append((teams[i], Team("BYE", 0)))
    return bracket

def seed_bracket(teams):
    teamsSorted = sorted(teams, key = lambda team: team.seed)
    n = len(teamsSorted)
    bracket = []
    for i in range(n // 2):
        bracket.append((teamsSorted[i], teamsSorted[n - 1 - i]))
    return bracket

def visualize(bracket):
    g = nx.DiGraph()
    pos = {}
    for i, (team1, team2) in enumerate(bracket):
        node = f"Match {i+1}"
        g.add_edge(team1.name, node)
        g.add_edge(team2.name, node)
        pos[team1.name] = (0, -i * 2)
        pos[team2.name] = (0, -i * 2 - 1)
        pos[node] = (1, -i * 2 - 0.5)

    plt.figure(figsize=(10, 8))
    nx.draw(g, pos, with_labels = True, node_color = "blue", node_size = 2000, font_size = 10, arrows = False)
    plt.title("Tournament Bracket")
    plt.axis("off")
    plt.show()

def getTeams():
    teams = []
    n = int(input("Enter: number of teams (must be even): "))
    print("Enter each team as TeamName,Seed (ex. Lakers,7)")
    for _ in range(n):
        entry = input("Team name and seed: ")
        try:
            name, seed = entry.split(",")
            teams.append(Team(name.strip(), int(seed.strip())))
        except:
            print("Invalid format.")
    return teams

if __name__ == "__main__":
    teams = getTeams()
    bracket = seed_bracket(teams)
    print("Final Bracket:")
    for i, match in enumerate(bracket, 1):
        print(f"Match {i}: {match[0].name} (Seed {match[0].seed}) vs {match[1].name} (Seed {match[1].seed})")

    visualize(bracket)
