---
title: Mimetic Tests
---

A mimetic is a kind of test which mimics the implementation of
the code rather than testing the behavior. They are a common
form of unit test.

![Like mimes, mimetic tests are a disappointment to their parents](https://upload.wikimedia.org/wikipedia/commons/a/a1/Nithor_Mime_Artist.jpg)

## How do you know if you've got a mimetic test?

A fully mimetic test fails when 100% of the failures
of the test are caused by code being changed
rather than the presence of a bug or lack of
desired functionality.

Note that [flakiness](flaky-tests) is different to mimeticism.

## What if a test fails 10% of the time solely because code changed?

Congratulations, your test is useful! In practice almost every
test will be at least slightly mimetic, so a small number of
failures caused by code changes is ok, provided this is
acknowledged as a bug (however minor).

## What's wrong with mimetic tests

Mimetic tests not only impose a cost in terms of the cost to
build, they also impose an ongoing maintenance cost as
changes to the code will require changes to tests.

Mimetic tests also don't catch much beyond the most trivial
bugs (e.g. syntax error).

A high proportion of mimetic tests often leads to 
[test case abandonment].

## Why does anybody write mimetic tests if they are so useless?

Mimetic tests tend to crop up when developers write code first and then
decide afterwards that their code needs some tests. They see classes
and think "I should write some tests for that class or method".
Sometimes these are [goodhart's tests](goodharts-tests).

Classes are implementation details. Methods are implementation
details. 

Unit tests lend themselves naturally to mimeticism simply
because they are inherently designed in such a way as to test
implementation rather than behavior.
