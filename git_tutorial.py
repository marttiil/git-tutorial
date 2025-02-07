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
              "\nAs a new wizard candidate, you should ask what are the team practices with branching."
              "\n\nBranchers are in fact simply pointers to a specific commit. Branch early, branch often.",
              "\nBecause of being a pointer, there is no storage/memory overhead with making them.",
              "\nBranch is just pointing to a specific commit in time.")
        
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
        print("In the simplest terms, git pull does a git fetch followed by a git merge.",
        "\n\ngit fetch gathers any commits from the target branch that do not exist",
        "\nin the current branch and stores them in your local repository.",
        "\nHowever, it does not merge them with your current branch.",
        "\nThis is particularly useful if you need to keep your repository up to date,",
        "\nbut are working on something that might break if you update your files.",
        "\nTo integrate the commits into your current branch, you must use git merge afterwards.")

    def tell_about_diff(self):
        print("git diff compares two commits (snapshots of repo) to each other and shows differences.")

    def tell_about_checkout(self):
        print("Git checkout is used to switch between branches. The command is bit complex...",
              "\nRemember,that when you before you commit, you need to stage stuff.",
              "\nWhen you call checkout, this staging or indexing area is filled.")

    def tell_about_commits(self):
        print("Git repo is basically a large database of commits. Each commit has a big ugly hash",
              "\nCommit contains also full snapshot of every file. They also store metadata, info about the commit (email of committer etc.)",
              "\nAnd very importantly, each commit stores a list of previous commit hash IDs.",
              "\nMost commits just store hash ID of the previous commit.",
              "\nAll info within commit is read-only, non-mutable."
              "\n\nGreat source: https://stackoverflow.com/questions/69826597/what-does-git-checkout-do")

    def tell_about_rebase(self):
        print("Rebasing is an alternative to merge with clear distinctions.",
              "\nRebasing essentially takes a set of commits, \"copies\" them, and plops them down somewhere else.",
              "\nPro of rebase: The commit log / history of the repository will be a lot cleaner if only rebasing is allowed!",
              "\nThink so that without rebase, commit history seems that the work was done sequentially, and with merge in parallel.",
              "Remember that rebase changes git history. That's an important difference to git merge.",
              "\n\nPRACTICALLY, you need to move to branch you want to rebase and use command git rebase <name-of-target-branch>")

    def tell_about_pull_request(self):
        # TODO : tell about pull_requests
        print("")

    def tell_about_merge(self):
        # TODO: Tell about merge
        print("")

    def tell_about_common_git_workflows(self):
        print("")

    def tell_cool_stuff_about_git(self):
        print("\n Cool fact 1 : Git repo is to a large extent just a big database of commits.")

    def tell_about_detached_head(self):
        print("HEAD is a pointer to the current commit. It is used as a reference point when you want to see last changes to your working copy with git diff",
              "\nThings get complicated when you checkout something that is not a branch. This happens because it CAN BE useful sometimes to switch from branch to commit itself.",
              "\nWhen you commit here, they will end up in the garbage sooner or later. They are not important.",
              "\n\nHOW TO END UP HERE?\n",
              "\nFew ways: git checkout <commit ID>/HEAD^/tag. Tag is supposed ot be immutable and are not updated as branches.",
              "\nThat's why this happened to you when you tried git checkout origin",
              "\n\nWHAT TO DO IF THIS HAPPENS?\n",
              "\nTake a deep breath, and read the CLI instructions :)")

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