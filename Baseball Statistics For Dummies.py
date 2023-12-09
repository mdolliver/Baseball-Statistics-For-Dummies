#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
csv_file_path = "Statsforproject_New.csv"
try:
  # Read the CSV file into a DataFrame
  df = pd.read_csv(csv_file_path)
except FileNotFoundError:
  print(f"The file '{csv_file_path}' was not found.")
except Exception as e:
  print(f"An error occurred: {e}")
#create lists of stats, 1 for basic, 1 for advanced
basic_stats = ['AB', 'H', 'HR', 'SO', 'AVG', 'SLG', 'OBP', 'OPS', 'RBI', 'R', 'TB', 'SB', 'CS', 'SB%']
advanced_stats = ['BACON', 'Barrels', 'Barrel%', 'OAA', 'Sprint Speed']
#create welcome message and spacing for later
print('Welcome to Baseball Statistics for Dummies')
print('(Statistics are for Qualified Batters with 500 plate appearances)')
print('Data from baseballsavant.mlb.com')
print_spacing = str('------------------------------------------------------------------\n')
while True:
  Q1 = input('What type of stats would you like to know more about: Basic Stats or Advanced Stats?\nAccepted Answers are "Basic Stats" or "Advanced Stats" ')
  while Q1 != 'Basic Stats' and Q1 != 'Advanced Stats':
    Q1 = input("Error: Invalid input. Please select 'Basic Stats' or 'Advanced Stats'.\nPlease enter either Basic Stats or Advanced Stats: ")
  print(print_spacing)
  if Q1 == 'Basic Stats':
      while True:
          print(f'List of Basic Stats: {basic_stats}')
          B1 = input('What basic stat would you like to know more about?: ')
          print(print_spacing)
          if B1 in basic_stats:
              break
          else:
              print('Error: Invalid input, please try again')
              print(print_spacing)
  
      # Now you can proceed with the valid input in the B1 variable
      if B1 == 'AB':
          print("In baseball, an at-bat (AB) or time at bat is a batter's turn batting against a pitcher. An at-bat is different from a plate appearance.")
          print("An at-bat is counted when:")
          print('-The batter reaches first base on a hit')
          print('-The batter reaches first base on an error')
          print('-The batter is called out for any reason other than a sacrifice')
          print("-There is a fielder's choice")
          print('There is no formula for calculating At Bats, At Bats are recorded and totaled.')
          print(print_spacing)
          print("The Batter with the most At Bats in the 2023 MLB Season was: Marcus Semien with 670 At Bats.")
          print(df[["last_name, first_name", "ab"]][df.ab==df.ab.max()])
          print(print_spacing)
          print("Here are the top 10 players in the At Bats category for the 2023 season")
          print(print_spacing)
          top_players = df.nlargest(10, 'ab')  # You can replace 'home_run' with the desired statistic
          plt.bar(top_players['last_name, first_name'], top_players['ab'])  # Replace 'home_run' accordingly
          bars= plt.bar(top_players['last_name, first_name'], top_players['ab'])
          plt.title('Top 10 Players - At Bats')  # Customize the title
          plt.xlabel('Player')
          plt.ylabel('At Bats')
          plt.xticks(rotation=45, ha='right')  
          for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
          plt.tight_layout()
          plt.show()
      elif B1 == 'H':
          print("H or Hits")
          print("A hit occurs when a batter strikes the baseball into fair territory and reaches base without doing so via an error or a fielder's choice.")
          print('There is no formula for calculating hits, hits are recorded and totaled.')
          print('There are four types of hits in baseball: singles, doubles, triples, and home runs. All four are counted equally when deciphering batting average.')
          print(print_spacing)
          print("The Batter with the most Hits in the 2023 MLB Season was: Ronald Acuna Jr. with 217 Hits.")
          print(df[["last_name, first_name", "hit"]][df.hit==df.hit.max()])
          print(print_spacing)
          print("Here are the top 10 players in the Hits category for the 2023 season")
          print(print_spacing)
          top_players = df.nlargest(10, 'hit')  # You can replace 'home_run' with the desired statistic
          plt.bar(top_players['last_name, first_name'], top_players['hit'])  # Replace 'home_run' accordingly
          bars= plt.bar(top_players['last_name, first_name'], top_players['hit'])
          plt.title('Top 10 Players - Hits')  # Customize the title
          plt.xlabel('Player')
          plt.ylabel('Hits')
          plt.xticks(rotation=45, ha='right')  
          for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
          # Rotate x-axis labels for better visibility
          plt.tight_layout()
          plt.show()
      elif B1 == 'HR':
        print("HR or Home Runs")
        print('A home run occurs when a batter hits a fair ball and scores on the play without being put out or without the benefit of an error.')
        print('There is no formula for calculating Home Runs, Home Runs are recorded and totaled.')
        print(print_spacing)
        print("The Batter with the most Home Runs in the 2023 MLB Season was: Matt Olson with 54 Home Runs.")
        print(df[["last_name, first_name", "home_run"]][df.home_run==df.home_run.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Home Runs category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'home_run')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['home_run'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['home_run'])
        plt.title('Top 10 Players - Home Runs')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Home Runs')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'SO':
        print('SO or Strike Out')
        print('A strikeout occurs when a pitcher throws any combination of three swinging or looking strikes to a hitter. (A foul ball counts as a strike, but it cannot be the third and final strike of the at-bat. A foul tip, which is caught by the catcher, is considered a third strike.)')
        print('There is no formula for calculating Strike Outs, Strike Outs are recorded and totaled.')
        print(print_spacing)
        print("The Batter with the most Strikeouts in the 2023 MLB Season was: Kyle Shwarber with 215 Strikeouts.")
        print(df[["last_name, first_name", "strikeout"]][df.strikeout==df.strikeout.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Strikeouts category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'strikeout')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['strikeout'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['strikeout'])
        plt.title('Top 10 Players - Strikeouts')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Strikeouts')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
        
      elif B1 == 'AVG':
        print("Batting Average, represented by AVG. One of the oldest and most universal tools to measure a hitter's success at the plate, batting average is determined by dividing a player's hits by his total at-bats for a number between zero (shown as .000) and one (1.000). In recent years, the league-wide batting average has typically hovered around .250. ")
        print('AVG formula is as follows: AVG = H/AB')
        print(print_spacing)
        print("The Batter with the best Batting Average in the 2023 MLB Season was: Luis Arraez with an average of 0.354.")
        print(df[["last_name, first_name", "batting_avg"]][df.batting_avg==df.batting_avg.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Batting Average category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'batting_avg')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['batting_avg'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['batting_avg'])
        plt.title('Top 10 Players - Batting Average')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Batting Average')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'SLG':
        print('SLG or Slugging Percentage')
        print("Slugging percentage represents the total number of bases a player records per at-bat. Unlike on-base percentage, slugging percentage deals only with hits and does not include walks and hit-by-pitches in its equation.")
        print("Slugging percentage differs from batting average in that all hits are not valued equally.")
        print('SLG formula is as follows: SLG = (1B + 2Bx2 + 3Bx3 + HRx4)/AB')
        print(print_spacing)
        print("The Batter with the best Slugging Percentage in the 2023 MLB Season was: Shohei Ohtani with a percentage of 0.654.")
        print(df[["last_name, first_name", "slg_percent"]][df.slg_percent==df.slg_percent.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Slugging Percentage category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'slg_percent')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['slg_percent'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['slg_percent'])
        plt.title('Top 10 Players - Slugging Percentage')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Slugging Percentage')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'OBP':
        print('OBP or On-Base Percentage')
        print("OBP refers to how frequently a batter reaches base per plate appearance. Times on base include hits, walks and hit-by-pitches, but do not include errors, times reached on a fielder's choice or a dropped third strike.")
        print("A hitter's goal is to avoid making an out, and on-base percentage shows which hitters have accomplished that task the best.")
        print("OBP formula is as follows: OBP = (H + BB + HBP(Hit By Pitch)) ÷ (AB + BB + HBP + SF (Sacrifice Flies))")
        print(print_spacing)
        print("The Batter with the best On-Base Percentage in the 2023 MLB Season was: Ronald Acuna Jr. with a percentage of 0.416.")
        print(df[["last_name, first_name", "on_base_percent"]][df.on_base_percent==df.on_base_percent.max()])
        print(print_spacing)
        print("Here are the top 10 players in the On-Base Percentage category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'on_base_percent')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['on_base_percent'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['on_base_percent'])
        plt.title('Top 10 Players - On-Base Percentage')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('On Base Percentage')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'OPS':
        print("OPS is On-Base Plus Slugging percentage: OPS adds on-base percentage and slugging percentage to get one number that unites the two. It's meant to combine how well a hitter can reach base, with how well he can hit for average and for power.")
        print("OPS formula is as follows: OPS = OBP + SLG")
        print(print_spacing)
        print("The Batter with the best On-Base + Slugging Percentage in the 2023 MLB Season was: Shohei Ohtani with a percentage of 1.066.")
        print(df[["last_name, first_name", "on_base_plus_slg"]][df.on_base_plus_slg==df.on_base_plus_slg.max()])
        print(print_spacing)
        print("Here are the top 10 players in the OPS category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'on_base_plus_slg')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['on_base_plus_slg'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['on_base_plus_slg'])
        plt.title('Top 10 Players - OPS')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('OPS')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'RBI':
        print("Runners Batted In or RBI is a tally of a hitters ability to bring in runs for their team.")
        print("A batter is credited with an RBI in most cases where the result of his plate appearance is a run being scored. There are a few exceptions, however. A player does not receive an RBI when the run scores as a result of an error or ground into double play.")
        print("There is no formula for calculating RBI's, RBI's are recorded and totaled.")
        print(print_spacing)
        print("The Batter with the most RBI's in the 2023 MLB Season was: Matt Olson with 139 RBI's.")
        print(df[["last_name, first_name", "b_rbi"]][df.b_rbi==df.b_rbi.max()])
        print(print_spacing)
        print("Here are the top 10 players in the RBI category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'b_rbi')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['b_rbi'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['b_rbi'])
        plt.title('Top 10 Players - RBI')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('RBI')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'R':
        print('Run')
        print("A player is awarded a run if he crosses the plate to score his team a run. When tallying runs scored, the way in which a player reached base is not considered. If a player reaches base by an error or a fielder's choice, as long as he comes around to score, he is still credited with a run. If a player enters the game as a pinch-runner and scores, he is also credited with a run.")
        print("There is no formula for calculating Runs, Runs are recorded and totaled.")
        print(print_spacing)
        print("The Batter with the most Runs in the 2023 MLB Season was: Ronald Acuna Jr. with 149 Runs.")
        print(df[["last_name, first_name", "r_run"]][df.r_run==df.r_run.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Runs category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'r_run')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['r_run'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['r_run'])
        plt.title('Top 10 Players - Runs')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Runs')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'TB':
        print('TB or Total Bases')
        print('Total bases refer to the number of bases gained by a batter through his hits. A batter records one total base for a single, two total bases for a double, three total bases for a triple and four total bases for a home run.')
        print("There is no formula for calculating Total Bases, Total Bases are recorded and totaled.")
        print(print_spacing)
        print("The Batter with the most Total Bases in the 2023 MLB Season was: Ronald Acuna Jr. with 383 Total Bases.")
        print(df[["last_name, first_name", "b_total_bases"]][df.b_total_bases==df.b_total_bases.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Total Bases category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'b_total_bases')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['b_total_bases'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['b_total_bases'])
        plt.title('Top 10 Players - Total Bases')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Total Bases')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'SB':
        print('SB or Stolen Bases')
        print("A stolen base occurs when a baserunner advances by taking a base to which he isn't entitled. This generally occurs when a pitcher is throwing a pitch, but it can also occur while the pitcher still has the ball or is attempting a pickoff, or as the catcher is throwing the ball back to the pitcher.")
        print("A stolen base is not automatically credited when a runner advances during one of the aforementioned scenarios; the official scorer must also determine that the runner had been in attempt of a steal. For example, if a runner takes an extra base on a wild pitch or a passed ball, he is not awarded a stolen base. However, if he was attempting to steal as a wild pitch/passed ball was thrown, he is generally given credit for it.")
        print("There is no formula for calculating Stolen Bases, Stolen Bases are recorded and totaled.")
        print(print_spacing)
        print("The Runner with the most Stolen Bases in the 2023 MLB Season was: Ronald Acuna Jr. with 73 Stolen Bases.")
        print(df[["last_name, first_name", "r_total_stolen_base"]][df.r_total_stolen_base==df.r_total_stolen_base.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Stolen Bases category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'r_total_stolen_base')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['r_total_stolen_base'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['r_total_stolen_base'])
        plt.title('Top 10 Players - Stolen Bases')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Stolen Bases')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'CS':
        print('CS or Caught Stealing')
        print("A caught stealing occurs when a runner attempts to steal but is tagged out before reaching second base, third base or home plate. This typically happens after a pitch, when a catcher throws the ball to the fielder at the base before the runner reaches it. But it can also happen before a pitch, typically when a pitcher throws the ball to first base for a pickoff attempt but the batter has already left for second.")
        print("There is no formula for calculating Caught Stealing, Caught Stealing(s) are recorded and totaled.")
        print(print_spacing)
        print("The Runner that has been Caught Stealing the most in the 2023 MLB Season was: Bobby Witt Jr. with 15 times being caught.")
        print(df[["last_name, first_name", "r_total_caught_stealing"]][df.r_total_caught_stealing==df.r_total_caught_stealing.max()])
        print(print_spacing)
        print("Here are the top 10 players in the Caught Stealing category for the 2023 season")
        print(print_spacing)
        top_players = df.nlargest(10, 'r_total_caught_stealing')  # You can replace 'home_run' with the desired statistic
        plt.bar(top_players['last_name, first_name'], top_players['r_total_caught_stealing'])  # Replace 'home_run' accordingly
        bars= plt.bar(top_players['last_name, first_name'], top_players['r_total_caught_stealing'])
        plt.title('Top 10 Players - Caught Stealing')  # Customize the title
        plt.xlabel('Player')
        plt.ylabel('Caught Stealing')
        plt.xticks(rotation=45, ha='right')  
        for bar in bars:
          yval = bar.get_height()
          plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
        # Rotate x-axis labels for better visibility
        plt.tight_layout()
        plt.show()
      elif B1 == 'SB%':
        print('SB% or Stolen Base Percentage')
        print("Stolen-base percentage is determined by the number of steals for a player divided by his total number of attempts. SB% is an essential tool in evaluating base stealers, because the league leaders in stolen bases often get thrown out frequently, too. In that vein, stolen bases are useful -- but only if a base stealer isn't at a high risk of getting thrown out.")
        print("SB% formula is as follows: SB% = SB / (SB+CS) ")
        print(print_spacing)
        print("An example of showing SB% is: Ronald Acuna Jr. had 73 SB's and was caught stealing 14 times. So his SB% is 73/(73+14) = 0.84 or 84%")
        print(print_spacing)
  elif Q1 == 'Advanced Stats':
      # Add code to handle advanced stats
    while True:
      print(f'List of Advanced Stats: {advanced_stats}')
      A1 = input('What advanced stat would you like to know more about?: ')
      print(print_spacing)
      if A1 in advanced_stats:
        break
      else:
        print('Error: Invalid input, please try again')
        print(print_spacing)
        # Now you can proceed with the valid input in the B1 variable
    if A1 == 'BACON':
      print('Batting Average on Contact or BACON')
      print("Batting Average on CONtact (BACON) determines how often a batter gets a hit when he makes contact. Thus, walks, strikeouts, and hit batters are not included in the calculation.")
      print("A high BACON can be an indication that the batter makes consistently solid contact and/or uses his speed to beat out infield hits.")
      print("BACON formula is as follows: BACON = Hits / Batted Balls")
      print(print_spacing)
      print("The Batter with the best Bacon Percentage in the 2023 MLB Season was: Shohei Ohtani with a percentage of 0.423.")
      print(df[["last_name, first_name", "bacon"]][df.bacon==df.bacon.max()])
      print(print_spacing)
      print("Here are the top 10 players in the BACON category for the 2023 season")
      print(print_spacing)
      top_players = df.nlargest(10, 'bacon')  # You can replace 'home_run' with the desired statistic
      plt.bar(top_players['last_name, first_name'], top_players['bacon'])  # Replace 'home_run' accordingly
      bars= plt.bar(top_players['last_name, first_name'], top_players['bacon'])
      plt.title('Top 10 Players - BACON')  # Customize the title
      plt.xlabel('Player')
      plt.ylabel('BACON')
      plt.xticks(rotation=45, ha='right')  
      for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
      # Rotate x-axis labels for better visibility
      plt.tight_layout()
      plt.show()
    elif A1 == 'Barrels':
      print('Barrels')
      print("The Barrel classification is assigned to batted-ball events whose comparable hit types (in terms of exit velocity and launch angle) have led to a minimum .500 batting average and 1.500 slugging percentage since Statcast was implemented Major League wide in 2015.")
      print("To be Barreled, a batted ball requires an exit velocity of at least 98 mph. At that speed, balls struck with a launch angle between 26-30 degrees always garner Barreled classification. For every mph over 98, the range of launch angles expands.")
      print(print_spacing)
      print('Examples of Barrels:')
      print("For example: A ball traveling 99 mph always earns 'Barreled' status when struck between 25-31 degrees. Add one more mph -- to reach 100 -- and the range grows another three degrees, to 24-33.")
      print("Every additional mph over 100 increases the range another two to three degrees until an exit velocity of 116 mph is reached. At that threshold, the Barreled designation is assigned to any ball with a launch angle between eight and 50 degrees.")
      print("There is no formula for calculating Barrels, Barrels are recorded and totaled.")
      print(print_spacing)
      print("The Batter with the most barrels in the 2023 MLB Season was: Ronald Acuna Jr. with 86 barrels.")
      print(df[["last_name, first_name", "barrel"]][df.barrel==df.barrel.max()])
      print(print_spacing)
      print("Here are the top 10 players in the Barrels category for the 2023 season")
      print(print_spacing)
      top_players = df.nlargest(10, 'barrel')  # You can replace 'home_run' with the desired statistic
      plt.bar(top_players['last_name, first_name'], top_players['barrel'])  # Replace 'home_run' accordingly
      bars= plt.bar(top_players['last_name, first_name'], top_players['barrel'])
      plt.title('Top 10 Players - Barrels')  # Customize the title
      plt.xlabel('Player')
      plt.ylabel('Barrels')
      plt.xticks(rotation=45, ha='right')  
      for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
      # Rotate x-axis labels for better visibility
      plt.tight_layout()
      plt.show()
    elif A1 == 'Barrel%':
      print('Barrel% or Barrel Percentage')
      print('Refer to the Barrel statistic to figure out what barrels are and how they are totaled')
      print("Barrel% formula is as follows: Barrel% = Barrels / Hit in Play")
      print(print_spacing)
      print("The Batter with the best Barrel Percentage in the 2023 MLB Season was: Shohei Ohtani with a percentage of 19.6%.")
      print(df[["last_name, first_name", "barrel_batted_rate"]][df.barrel_batted_rate==df.barrel_batted_rate.max()])
      print(print_spacing)
      print("Here are the top 10 players in the Barrel Percentage category for the 2023 season")
      print("Press the 'X' in the top right of the graph to continue.")
      print(print_spacing)
      top_players = df.nlargest(10, 'barrel_batted_rate')  # You can replace 'home_run' with the desired statistic
      plt.bar(top_players['last_name, first_name'], top_players['barrel_batted_rate'])  # Replace 'home_run' accordingly
      bars= plt.bar(top_players['last_name, first_name'], top_players['barrel_batted_rate'])
      plt.title('Top 10 Players - Barrel%')  # Customize the title
      plt.xlabel('Player')
      plt.ylabel('Barrel%')
      plt.xticks(rotation=45, ha='right')  
      for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
      # Rotate x-axis labels for better visibility
      plt.tight_layout()
      plt.show()
    elif A1 == 'OAA':
      print('OAA or Outs Above Average')
      print('Outs Above Average (OAA) is a range-based metric of skill that shows how many outs a player has saved. Prior to 2020, OAA was an outfield-only metric. But it has been expanded to include infielders. OAA is calculated differently for outfielders and infielders.')
      print(print_spacing)
      print('Outfield OAA:')
      print("Outs Above Average for outfielders starts with Catch Probability, which takes the distance an outfielder must go, the time he has to get there, and the direction he travels to put a percentage of catch likelihood on each individual batted ball. OAA for outfielders is the season-long cumulative expression of each individual Catch Probability play. For example, if an outfielder has a ball hit to him with a 75 percent Catch Probability -- that is, one an average outfielder would make three-quarters of the time -- and he catches it, he'll receive a +.25 credit. If he misses it, he'll receive -.75, reflecting the likelihood of that ball being caught by other outfielders.")
      print(print_spacing)
      print('Infield OAA')
      print("Outs Above Average for infielders takes the following factors into account.")
      print("• How far the fielder has to go to reach the ball ('the intercept point').")
      print("• How much time he has to get there.")
      print("• How far he then is from the base the runner is heading to.")
      print("• On force plays, how fast the batter is, on average. (A runner's average Sprint Speed is used in the calculation, rather than his Sprint Speed on that particular play. For new players with no data, a league-average -- 27 ft/sec -- score is used; once the player qualifies for the leaderboard, all of his previous plays are re-run.)")
      print("There is no formula for calculating Outs Above Average, Outs Above Average are recorded and totaled. ")
      print(print_spacing)
      print("The Fielders with the best Outs Above Average in the 2023 MLB Season were: Luis Robert Jr. and Julio Rodriguez with 12 Outs Above Average each.")
      print(df[["last_name, first_name", "n_outs_above_average"]][df.n_outs_above_average==df.n_outs_above_average.max()])
      print(print_spacing)
      print("Here are the top 10 players in the Outs Above Average category for the 2023 season")
      print(print_spacing)
      top_players = df.nlargest(10, 'n_outs_above_average')  # You can replace 'home_run' with the desired statistic
      plt.bar(top_players['last_name, first_name'], top_players['n_outs_above_average'])  # Replace 'home_run' accordingly
      bars= plt.bar(top_players['last_name, first_name'], top_players['n_outs_above_average'])
      plt.title('Top 10 Players - OAA')  # Customize the title
      plt.xlabel('Player')
      plt.ylabel('Outs Above Average')
      plt.xticks(rotation=45, ha='right')  
      for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
      # Rotate x-axis labels for better visibility
      plt.tight_layout()
      plt.show()
    elif A1 == 'Sprint Speed':
      print('SS or Sprint Speed')
      print("Introduced during the 2017 season, Sprint Speed is a Statcast metric that aims to more precisely quantify speed by measuring how many feet per second a player runs in his fastest one-second window.")
      print("Currently, the metric includes 'qualified runs' from these two categories:\n• Runs of two bases or more on non-homers, excluding runs from second base when an extra-base hit happens.\n• Home-to-first runs on 'topped' or 'weakly hit' balls.\nThe best of these runs, approximately two-thirds, are averaged for a player's seasonal average.\nAny run with a Sprint Speed of at least 30 ft/sec is known as a Bolt.")
      print(print_spacing)
      print('Why Its Useful:')
      print('Approximately seven full-effort strides can be captured over the course of a one-second window, so Sprint Speed rewards those who can sustain their speed over a longer period of time.')
      print("There is no formula for calculating Sprint Speed, Sprint Speed is recorded and averaged. ")
      print(print_spacing)
      print("The Runner with the best Sprint Speed in the 2023 MLB Season was: Bobby Witt Jr, with a top sprint speed of 30.5 Feet/Sec")
      print(df[["last_name, first_name", "sprint_speed"]][df.sprint_speed==df.sprint_speed.max()])
      print(print_spacing)
      print("Here are the top 10 players in the Sprint Speed category for the 2023 season")
      print(print_spacing)
      top_players = df.nlargest(10, 'sprint_speed')  # You can replace 'home_run' with the desired statistic
      plt.bar(top_players['last_name, first_name'], top_players['sprint_speed'])  # Replace 'home_run' accordingly
      bars= plt.bar(top_players['last_name, first_name'], top_players['sprint_speed'])
      plt.title('Top 10 Players - Sprint Speed')  # Customize the title
      plt.xlabel('Player')
      plt.ylabel('Sprint Speed')
      plt.xticks(rotation=45, ha='right')  
      for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
      # Rotate x-axis labels for better visibility
      plt.tight_layout()
      plt.show()
      
  else:
    print("Error: Invalid input. Please select 'Basic Stats' or 'Advanced Stats'.")
  continue_q = input("Press Enter if you would like to run the program again.")


# In[ ]:




