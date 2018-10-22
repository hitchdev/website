---
title: HitchDev Principles
---

The HitchDev framework is committed to the following principles:

* Automated consistent dev and test environment setup - there should be fewer than 5 steps to get the average dev or test environment set up.
* Executable specifications should define the behavior of projects only - where this becomes cumbersome, it's a sign that the project should be broken into subprojects.
* The specifications should be terse and strongly typed.
* The projects should be tested against a realistic a model of the real world they will face as possible.
* There should be strict separation of concerns between descriptive executable stories and the the execution engine used to actually execute them.
* The execution engine should set up a realistic, isoated environment that runs the code and interacts with it, keeping a clean separation between "mock real world" and "code under test".
* Documentation should be *generated* from specifications and specifications should explain themselves clearly in order to generate better documentation.
