---
title: Code quality principles
---

Improved code quality is about reduced code maintenance costs. Code quality consideration is *not* a religious exercise, it is a budgeting exercise.

Code that does what the user wants is typically the highest priority. These principles are not about that. These principles are about code qualities that are *not about* what the user wants. "Fast" and "bug free" are thus not listed, even though most of the time, it's easier to get faster and bug free code if your code is clean.

All of the principles here are important but they ought to be applied on a cost/benefit basis. They are all trade offs. There is *sometimes* a right answer (when improving code quality incurs a very small cost, you should always do it). There is sometimes no right answer.

Therefore:

* If maintenance costs of your system are not important, *these principles may not be either*.
* Building the wrong thing in the right way slowly is *far* worse than building the wrong thing in the wrong way quickly.
* Functional requirements (features, bugs, speed) usually take precedence over maintenance cost.
* Everything here is a trade off - you cannot be religious about any aspect of code quality. Perfectionism with respect to code quality is a curse.
* They will conflict (e.g. some code might have higher cohesion but not be as DRY) and in such cases the costs and benefit of following each principle should be acknowledged before deciding which one to prioritize.

Principles:

1. [Write the least code](write-least-code) possible
2. [Isolation](isolate) code as much as possible.
3. Use language that uses the [least expressive power](least-expressive-power) necessary
4. [Fail fast and fail clearly](fail-fast-and-fail-clearly)
5. [Automate](automation) repetitive development tasks
6. Write code with [high cohesion](high-cohesion)
7. Write [deterministic code](deterministic)
8. Write code in a [consistent way](consistency)
9. Write code with clear [naming](naming)
