from random import randrange

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
        
    def tell_about_push(self):
        print("\n Push is a command to push local commits to a remote repository.",
              "\nThis makes the local commits accessible to your team members"
              "\n\n COMMON WORK FLOW\n",
              "\ngit add . OR <name of the file>",
              "\ngit commit -m \"commit message\")",
              "\ngit push <remote URL or alias-of-target-repo>",
              "\n\ANOTHER WAY\n",
              "\ngit add .",
              "\ngit commit -m <\"message\">",
              "git fetch <URL OR alias-of-target-repo> name # This command fetches the latest version of target repo",
              "\ngit rebase # Ask more about fetch and rebase from me specifically... Wizard must be short in answers.",
              "\ngit push --force # ONLY USE FORCE AFTER FETCH-REBASE")
        
    def tell_about_fetch(self):
        # TODO: tell about fetching...
        print("")

    def tell_about_rebase(self):
        # TODO : tell about rebasing...
        print("")

    def tell_about_pull_request(self):
        # TODO : tell about pull_requests
        print("")

    def tell_about_merge(self):
        # TODO: Tell about merge
        print("")

    def tell_about_common_git_workflows(self):
        print("")

    def cast_a_spell(self):
        spellNo = randrange(3)

        if spellNo == 0:
            print("\nAvadakedav... jkd. Rictusempra!")
        elif spellNo == 1:
            print("\nHokkus Pokkus!")
        elif spellNo == 2:
            print("\nWizard casted a spell.\nAll you worries were removed for the next 24 hours. Have a nice day.")

wizard = gitWizard(1000)
wizard.tell_about_branching()

wizard.cast_a_spell()