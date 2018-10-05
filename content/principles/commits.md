---
Title: Commit messages and their meanings
---

Each commit message in hitchdev projects takes the form TYPE : Message.

## BUGFIX

Bugfix on implemented feature that does not intentionally impact pre-existing defined
behavior. Should typically come with a story or change to a story that invokes the behavior
that failed before the bug was fixed.


## FEATURE

Newly implemented feature that does not intentionally impact pre-existing defined
behavior. Should come accompanied with a story or change to a story that invokes
and describes the behavior.

## REFACTOR

Changes to code that do not intentionally impact behavior. All code changes
should be covered by stories. Does not need to come accompanied with story.


## TOOLING

Changes to the tooling code - e.g. how tests run, linting, etc.

No changes to actual code of the project.

## DOCS

Changes to documentation page, documentation templates or non-functional changes
to stories intended to clarify the documentation.


## STORY

Adding new stories (e.g. features not previously covered) or changing existing
ones.

## RELEASE

Commit message of form "0.3.0 -> 0.3.1".

This is an automatically generated commit created by the "deploy" command.


## BACKWARDS INCOMPATIBLE REFACTOR

A refactoring that is not intended to change the functionality of the project and will break existing APIs. This will typically be done to make publicly facing APIs cleaner or remove functionality deemed unnecessary.

One or more commits should involve the project version changing like so:

- For project still in alpha : 0.3.5 -> 0.4.0 (minor version bump)
- For project out of alpha : 1.3.4 -> 2.0.0 (major version bump)


## BACKWARDS INCOMPATIBLE FEATURE

A feature that deliberately breaks existing functionality.


## BACKWARDS INCOMPATIBLE BUGFIX

A bugfix that deliberately breaks existing functionality.


## MISC

Anything that does not appear in one of the above categories. These should be rare.

