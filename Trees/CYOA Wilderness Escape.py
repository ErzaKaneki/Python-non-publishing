class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) != 0:
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
                    2) Yell 'Hooray!'\n""")

choice_b = TreeNode("""
You come across a clearing full of flowers.
The bear follows you and asks 'What gives?'\n
                    Do you:
                    1) Gasp 'A talking bear!'
                    2) Explain that the bear scared you.\n""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week.\nAfter making peace with a talking bear, he shows you the way out of the forest.\n\n
                    YOU HAVE ESCAPED THE WILDERNESS.""")
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.\n\n
                    YOU REMAIN LOST.""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b_1 = TreeNode("""
The bear is unamused.  After smelling the flowers,\nit turns around and leaves you alone.\n\n
                    YOU REMAIN LOST.""")
choice_b_2 = TreeNode("""\nThe bear understands and apologizes for startling you.\nYour new friend shows you a path leading out of the forest.\n\n
                    YOU HAVE EXCAPED THE WILDERNESS.""")

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

TreeNode.traverse(story_root)