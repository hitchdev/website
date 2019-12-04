---
title: The Mirror Test
---

The mirror test is a kind of test which *mirrors* the implementation of
the code rather than testing the behavior. They are most typically
unit tests.

## How do you know if you've got a mirror test?

A key defining feature of a mirror test is that it
*fails when the code under test has changed*
irrespective of whether or not there is a bug.

Mirror tests not only impose a cost in terms of the cost to
build, they also impose an ongoing maintenance cost as
changes to the code 


## Why does anybody write mirror tests?

Mirror tests tend to crop up when developers write code first and then
decide afterwards that their code needs some tests. They see classes
and think "I should write some tests for that class". This "locks down"
the implementation.
