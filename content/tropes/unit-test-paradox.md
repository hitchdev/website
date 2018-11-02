---
title: The Unit Test Paradox
---

The unit test paradox is the paradox that low level unit testing "drives"
good design by *itself* being a form of bad design.

## Low level unit tests tightly couple to code

All tests couple to something - end to end tests couple to the body
of the architecture as a whole. Lower level integration tests couple to
lower level implementation details.

The lower the level of the testing, the *tighter* it couples to the
implementation.

## Coupling == pain

If you have worked on tightly coupled software or "spaghetti code"
you will understand the pain of trying to understand 
