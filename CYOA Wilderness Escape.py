class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

user_choice = input("What is your name?  ")

story_root = TreeNode("""You are in a forest clearing.\nThere is a path to the left.
A bear emerges from the trees and roars!\n
                      Do you:
                      1) Roar back!
                      2) Run to the left...
                      """)
print(story_root.story_piece)