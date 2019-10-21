---
title: The least code principle
---

{{< warning title="Axiomatic trade off quality" >}}
This principle is both a [trade off and axiomatic](../../).
{{< /warning >}}

Code (which includes specifications, documentation, comments, tests, configuration and regular code)
is both an asset but also a **liability**.

Steve McConnell in his book, Code Complete argues that bugs appear in proportion to code,
even going so far as to cite statistics from a study:

```
(a) Industry Average: "about 15 - 50 errors per 1000 lines of delivered
code." He further says this is usually representative of code that has some
level of structured programming behind it, but probably includes a mix of
coding techniques.
```

## Going too far

Perl is an old language that used to be more popular, but it somewhat dated now. It was
famous for its "one liners" which would compress a huge amount of complex functionality
into a very small number of characters:

```
($l=join("",<>))=~s/.*\n/index($`,$&)>=$[||print$&/ge;
```

From [Antipope](http://www.antipope.org/charlie/old/attic/perl/one-liner.html).

Part of this was because of the semantics of the perl programming language, which allowed
the ability to apply a command to different data types and do different things in context
as well as commands which combined fetching data with mutation. These are both examples
of increased language power.

## Subprinciples

There are a number of sub-principles which can be derived partly or wholly
from this principle.

* [DRY](dry)
* [Don't reinvent the wheel](dont-reinvent-the-wheel)
* [YAGNI](yagni)
