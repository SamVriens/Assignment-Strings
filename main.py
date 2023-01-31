# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
playerScored1 = 'Ruud Gullit'
playerScored2 = 'Marco van Basten'
goal_0 =  32
goal_1 =  54
scorers = (playerScored1 + ' ' + str (goal_0) + ', ' + playerScored2 + ' ' + str (goal_1 ))
report = (playerScored1 + " scored in the " + str (goal_0) +"nd minute\n" + playerScored2 + " scored in the " + str (goal_1) +"th minute")

player = "Frank Rijkaard"
first_name1 = player.find (" ") 
first_name = player[:5]             
last_name = player[6:] 
last_name_len = (len (last_name))
name_short1 = (player[0:1]) 
nameShort = (name_short1 + '. ' + last_name)
name_short = nameShort
chant = (first_name +'! ') * len (first_name[:-1]) + (first_name + '!') 
good_chant = (first_name + '! ') != (first_name + '!')


print(chant)

print(good_chant)







