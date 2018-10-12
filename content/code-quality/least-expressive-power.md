---
title: Write code with the least expressive power
---

Write code with the least expressive power necessary is a [tradeoff principle of code quality].

Examples
--------

* YAML vs Python
* The story of JSON
* Whither garbage collector
* Metaprogramming
* LINQ vs. C#
* SQL vs. imperative
* The DSL merry-go-round
* C++ templating language


Subprinciples
-------------

These are principles which can be partially or in whole be derived from this principle.

* Immutability vs. Mutability (side effects)
* State isolation
* Lazy evaluation
* [Principle of least privilege in protocol design](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

Other people talking about the same principle
---------------------------------------------

These explanations discuss languages as if their power is uniform and static, whereas this principle
also applies to problems and the power of features used to solve them within the same language.

* https://www.w3.org/DesignIssues/Principles.html#PLP (treats 'language power' as uniform across a programming language - although it can vary from feature to feature - e.g. functional vs. imperative).

* https://events.ccc.de/congress/2011/Fahrplan/events/4763.en.html (applied specifically to security)

* https://www.w3.org/2001/tag/doc/leastPower.html

* https://blog.codinghorror.com/the-principle-of-least-power/ Jeff Atwood
