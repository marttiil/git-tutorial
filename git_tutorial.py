

class gitWizard:
    def __init__(self, age):
        self.age = age

        print("*****************************************************************************",
              "************************************************************************")

    def tell_about_branching(self):
        print("\nBranching is a powerful git feature that a skilled git-user wants to master",
              "\nBranches are independent lines of work, stemming from the original database",
              "\n\nBRANCHING IN TEAMS\n",
              "\nIn professional setting, teams usually have own guidelines with branching.",
              "\nAs a new wizard candidate, you should ask what are the team practices with branching.a")


wizard = gitWizard(1000)
wizard.tell_about_branching()
