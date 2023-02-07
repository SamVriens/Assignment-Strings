# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_scored1 = 'Ruud Gullit'
player_scored2 = 'Marco van Basten'
goal_0 =  32
goal_1 =  54
scorers = player_scored1 + ' ' + str(goal_0) + ', ' + player_scored2 + ' ' + str(goal_1 )
report = f'{player_scored1} scored in the {str (goal_0)}nd minute\n{player_scored2} scored in the { str (goal_1)}th minute'

player = "Frank Rijkaard"
index_space = player.find (" ") 
first_name = player[:index_space]             
last_name = player[index_space+1:] 
last_name_len = len(last_name)
name_short1 = player[0]
name_short = name_short1 + '. ' + last_name
name_short = name_short
chant = (first_name +'! ') * len (first_name[:-1]) + (first_name + '!') 
good_chant = chant[-1] != " "

print(chant)
print(good_chant)





