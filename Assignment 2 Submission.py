"""
Jesus Zeno
Assignment 2
SIE 508
"""

"""
This is to set up the avatar class for a human-type avatar.
They will have attributes such as: name, hair color, height, gender, superpower. An Avatar object can
change its hair color and superpower. It also has a method that “animates” the avatar. The Animate()
method should print out the Avatar’s object variables.
"""

# Make Human avatar characters
class HumanAvatar:
    # Initialize the instance variables of each object
    def __init__(self, name, hair_color, height, gender, superpower):
        self.name = name
        self.hair_color = hair_color
        self.height = height
        self.gender = gender
        self.superpower = superpower

    # Function to change superpower
    def setSuperpower(self, superpower):
        self.superpower = str(superpower)

    # Function to change hair color
    def setHaircolor(self, hair_color):
        self.hair_color = str(hair_color)

    # Animate function to print out the object's variables
    def Animate(self):
        print("The character's name is {}.".format(self.name))
        print("{}\'s hair color is {}.".format(self.name, self. hair_color))
        print("{}\'s height is {}.".format(self.name, self.height))
        print("{}\'s gender is {}.".format(self.name, self.gender))
        print("{}\'s superpower is {}.".format(self.name, self.superpower))


"""
This is to setup the game class. The game object is initialized without avatars. Starting the game makes an 
empty list of avatars. An avatar can be added one by one to the game object. We can also animate all the current
avatars in the game object. Stopping the game will get rid of all the characters for the game. 
"""
# Make a game class
class Game:
    # Initialize the instance variables of the game object.
    def __init__(self, game_name):
        self.game_avatar_name_list = None
        self.game_name = game_name
        self.game_avatars = None

    # When the game is started up, make an internal empty list of avatar objects.
    def startGame(self):
        game_avatars = []
        self.game_avatars = game_avatars

    # Add one avatar at a time to the game avatar list.
    def addAvatar(self, super_hero):
        # Let's filter the results
        results = list(filter(lambda x: (x == super_hero), self.game_avatars))
        # If we find an existing item we raise an exception
        if results:
            print("{} avatar is already stored".format(super_hero.name))
        # If not, we append item to the list
        else:
            self.game_avatars.append(super_hero)
            # Give confirmation that a character has been added to which game.
            print("{} has been added to the game {}".format(super_hero.name, self.game_name))
        return

    # Helper function to just give us the names of the avatar objects
    def game_avatar_name(self):
        game_avatar_name_list = []
        self.game_avatar_name_list = game_avatar_name_list
        i = 0
        while i < len(self.game_avatars):
            self.game_avatar_name_list.append(self.game_avatars[i].name)
            i += 1
        return self.game_avatar_name_list

    # Animate all the character objects from the list of game avatars once.
    def gameAnimate(self):
        i = 0
        while i < len(self.game_avatars):
            print("Let's animate all of {}'s actions:".format(self.game_avatars[i].name))
            self.game_avatars[i].Animate()
            i += 1

    # Destroy all the avatar objects from the internal list.
    def stopGame(self):
        self.game_avatars = []
        print("These are now the avatars left in the game{}".format(self.game_avatars))


def main():
    # Initialize superhero objects
    Mario = HumanAvatar('Mario', 'black', '5ft 8 in', 'male', 'saving peach')
    Luigi = HumanAvatar('Luigi', 'black', '5ft 10in', 'male', 'best bro ever')
    Peach = HumanAvatar('Peach', 'blonde', '5ft 4in', 'female', 'looking fabulous')
    Toadette = HumanAvatar('Toadette', 'pink', '4ft 3in', 'female', 'mini golf')

    # Check that every hero can be animated
    Mario.Animate()
    Luigi.Animate()
    Peach.Animate()
    Toadette.Animate()

    # Check that we can change a character's powers and hair color.
    Mario.setSuperpower("Sunshine")  # Change Mario's power
    Mario.Animate()
    Peach.setHaircolor("Red")  # Change Peach's Hair to look like Daisy
    Peach.Animate()

    # Create super mario game object
    super_mario_game = Game('super-mario')
    print("The name of this game is: ", super_mario_game.game_name)

    # Start the game and clear out any characters that may be in the game previously.
    super_mario_game.startGame()

    # Check that the list of avatars is empty after starting up the game
    print("Checking game avatars list at start of game:\n", super_mario_game.game_avatar_name())

    # Add the four characters to the game
    super_mario_game.addAvatar(Mario)
    super_mario_game.addAvatar(Luigi)
    super_mario_game.addAvatar(Peach)
    super_mario_game.addAvatar(Toadette)

    # Check to see that we can't add a character twice.
    print("Can we add a character twice?")
    super_mario_game.addAvatar(Mario)

    # Check to see character was added to the game.
    print("Checking game avatars list while game is running:\n", super_mario_game.game_avatar_name())

    # Animate all the characters that have been added to the game.
    super_mario_game.gameAnimate()

    # Stop the game and get rid of any characters added to the game.
    super_mario_game.stopGame()

    # Check that all the characters have been eliminated from the game after stopping it.
    print("Checking game avatars list after game is stopped\n", super_mario_game.game_avatar_name())


if __name__ == '__main__':
    main()
