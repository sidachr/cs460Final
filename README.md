
Overview:
- This project generates and visualizes tournament brackets based on user-inputted teams and seeds/rankings, applying standard seed-based pairing rules. It is designed for organizing competitive tournaments in sports, esports, or other competitions.

Features:
- Accepts team names and seed/ranking values as input.
- Automatically pairs the teams into matchups for a seeded tournament bracket.
- Visualizes the bracket graphically using Matplotlib.
- Includes an automated test suite with non-trivial cases.
- Provides performace measurements

Instructions:
- The file 'algorithm.py' is the file with the alogrithm. The python file should work with a standard IDE.
- Run the program and you will see:
    'Enter: number of teams (must be even):'
- Enter an even number, since tournaments usually have an even number of teams.
- After the amount of teams is inputted you will see:
      Enter each team as TeamName,Seed (ex. Lakers,7)
      Team name and seed:
- Enter teams and seeds/rankings like the example given.
- The output will result in a bracket visualization along with an output with the matchups.
- For example:
  Match 1: Liverpool (Seed 1) vs Benfica (Seed 16)
  Match 2: Barcelona (Seed 2) vs Paris Saint-Germain (Seed 15)
  Match 3: Arsenal (Seed 3) vs PSV Eindhoven (Seed 14)
  Match 4: Inter Milan (Seed 4) vs AC Milan (Seed 13)
  Match 5: Atlético Madrid (Seed 5) vs Bayern Munich (Seed 12)
  Match 6: Bayer Leverkusen (Seed 6) vs Real Madrid (Seed 11)
  Match 7: Lille (Seed 7) vs Borussia Dortmund (Seed 10)
  Match 8: Aston Villa (Seed 8) vs Atalanta (Seed 9)
