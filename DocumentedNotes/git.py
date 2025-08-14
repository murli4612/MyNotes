Git Merge vs. Git Rebase
Both git merge and git rebase are used to integrate changes from one branch into another, but they work differently.

1. Git Merge
git merge creates a new commit that combines the histories of two branches.

Example: Merging feature into main

git checkout main
git merge feature


This creates a merge commit that combines changes from both branches.
It preserves the commit history of the feature branch.
Useful for collaborative workflows where history needs to be maintained.

Example Merge Flow
A---B---C (main)
     \
      D---E (feature)

After merge:
A---B---C---F (main)
     \     /
      D---E (feature)

Pros: Preserves history, easy to track changes.
Cons: Creates extra merge commits, making history more complex.

2. Git Rebase
git rebase rewrites the commit history by moving a branch on top of another.

Example: Rebasing feature onto main
git checkout feature
git rebase main


It moves all commits from feature to the latest main.
No extra merge commits are created.
It makes history linear and clean

Example Rebase Flow

Before rebase:
A---B---C (main)
     \
      D---E (feature)

After rebase:
A---B---C (main)
         \
          D'---E' (feature, rebased)

Cons: Can cause conflicts; not ideal for shared branches.


3. When to Use Merge vs. Rebase
Scenario	Use Merge	Use Rebase
Keeping full history	✅ Yes	❌ No
Avoiding extra commits	❌ No	✅ Yes
Working on a shared branch	✅ Yes	❌ No
Making history clean	❌ No	✅ Yes


4. Handling Conflicts
If conflicts occur during merge:
 
git merge feature
# Resolve conflicts
git add .
git commit -m "Resolved merge conflicts"



If conflicts occur during rebase:

git rebase main
# Resolve conflicts
git add .
git rebase --continue



5. Interactive Rebase
To edit, squash, or remove commits:

git rebase -i HEAD~3


This opens an interactive editor to modify commit history.

Conclusion
Use git merge for collaborative workflows and to keep full commit history.
Use git rebase to create a clean, linear history, especially for private branches.

