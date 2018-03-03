---
title: Code quality principles
---

These are our set of non-functional code quality principles. I wrote them as a guide for the kind of thing I'm looking for in pull requests. They may have broader applicability than that.

Note that these principles are all *trade offs* and their application should always be cost/benefit driven.

Therefore:

* Code quality principles should *not* be applied religiously.
* They will conflict (e.g. some code might have higher cohesion but not be as DRY) and in such cases the costs and benefit of following each principle should be acknowledged before deciding which one to prioritize.
* Perfectionism is a curse. It's often better to get code out there and used instead of obsessing over its quality.
* Building the wrong thing in the right way slowly is *far* worse than building the wrong thing in the wrong way quickly.

Principles:

1. [Write the least code](write-least-code) possible
2. [Loosely couple](loose-coupling) all interacting code
3. Use language that uses the [least expressive power](least-expressive-power) necessary
4. [Fail fast and fail clearly](fail-fast-and-fail-clearly)
5. [Automate](automation) repetitive development tasks
6. Write code with [high cohesion](high-cohesion)
7. Write [deterministic code](deterministic)
8. Write code in a [consistent way](consistency)
9. Write code with clear [naming](naming)
