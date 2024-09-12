class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while story_node.choices is not None:
            choice = input("Enter 1 or 2 to continue the story: ")
            valid_options =["1", "2"]
            while choice not in valid_options:
                choice = input("Please make a valid selection of 1 or 2")
            chosen_index = int(choice) - 1
            chosen_child = story_node.choices[chosen_index]
            print(chosen_child.story_piece)
            story_node = chosen_child


# user_choice = input("What is your name?  ")
# print("\n\n" + user_choice + ",")

story_root = TreeNode("""You are in a forest clearing.\nThere is a path to the left.
A bear emerges from the trees and roars!\n
                    Do you:
                    1) Roar back!
                    2) Run to the left...
                    """)

choice_a = TreeNode("""
The bear is startled and runs away.\n
                    Do you:
                    1) Shout 'Sorry bear!'
                    2) Yell 'Hooray!'""")

choice_b = TreeNode("""
You come across a clearing full of flowers.
The bear follows you and asks 'What gives?'\n
                    Do you:
                    1) Gasp 'Atalking bear!'
                    2) Explain that the bear scared you.""")
story_root.add_child(choice_a)
story_root.add_child(choice_b)

TreeNode.traverse(story_root)