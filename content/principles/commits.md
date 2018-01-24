---
Title: Commit messages and their meanings
---

Each commit message takes the form TYPE : Message.

These messages are, in a sense, alpha. They take effect on March 1st, 2018:

TOOLING
-------

Changes to the tooling code. No changes to actual code of the project.

Changes to project code : no

DOCS
----

Changes to documentation page or documentation template.

Changes to project code : no

STORY
-----

Refactoring of an existing story, its metadata, names, etc.

Changes to project code : no

REFACTOR PATCH 
--------------

Changes to code that do not intentionally impact defined behavior. All code changes
should be covered by stories. Does not need to come accompanied with story.

Changes to project code : yes

BACK COMPATIBLE FEATURE
-----------------------

Newly implemented feature that does not intentionally impact pre-existing defined
behavior. Should come accompanied with a story or change to a story that invokes
and describes the behavior.

Changes to project code : yes

BACK COMPATIBLE BUGFIX
----------------------

Bugfix on implemented feature that does not intentionally impact pre-existing defined
behavior. Should typically come with a story or change to a story that invokes the behavior
that failed before the bug was fixed.

Changes to project code : yes


BACKWARDS INCOMPATIBLE REFACTOR
-------------------------------

A refactoring that is not intended to change the functionality of the project and will break existing APIs. This will typically be done to make publicly facing APIs cleaner or remove functionality deemed unnecessary.

One or more commits should involve the project version changing like so:

- For project still in alpha : 0.3.5 -> 0.4.0 (minor version bump)
- For project out of alpha : 1.3.4 -> 2.0.0 (major version bump)

Changes to project code : yes

BACKWARDS INCOMPATIBLE FEATURE
------------------------------

A feature that deliberately breaks existing functionality.

Changes to project code : yes

BACKWARDS INCOMPATIBLE BUGFIX
-----------------------------

A bugfix that deliberately breaks existing functionality.

Changes to project code : yes

RELEASE
-------

Commit message of form "0.3.0 -> 0.3.1".

This should *only* be an automatically generated commit created by the "deploy" command.

MISC
----

Anything that does not appear in one of the above categories. These should be rare. If they
become too common it indicates that another commit type is necessary.


