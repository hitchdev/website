---
title: HitchDev
weight: 0
type: index
---

HitchDev is a group of self contained, heavily dogfooded python libraries - mainly used for setting up and running dev and test environments:

Fully documented general tools:

- [StrictYAML](strictyaml) -- YAML parser and validator that parses a restricted subset of the YAML spec.
- [Commandlib](commandlib) - invoke UNIX commands with an easy to use, pythonic API.

Fully documented testing projects:

- [HitchStory](hitchstory) -- StrictYAML based BDD framework.
- [HitchRunPy](hitchrunpy) - tool to invoke and run snippets of python code.
- [SeleniumDirector](seleniumdirector) -- declare page (CSS/ID/xpath/etc.) selectors and give them readable names which can be used in readable python code or tests.

Projects that will be documented soon:

- [pathquery](https://github.com/crdoconnor/pathquery) - declaratively API to recursively search for files.
- [dirtemplate](https://github.com/hitchdev/dirtemplate) - create and build templated directories using jinja2 (used for documentation generation).
- [pretendsmtp](https://github.com/hitchdev/pretendsmtp) - mock SMTP server.
- [templex](https://github.com/crdoconnor/templex) - templated regex matcher
- [faketime](https://github.com/crdoconnor/commandlib) - tool to lie to running processes (e.g. CPython or postgres) about the current system time.
- [xeger](https://github.com/crdoconnor/xeger) - generate strings from regular expressions.
- [icommandlib](https://github.com/crdoconnor/icommandlib) - extension to commandlib to invoke and interact with running UNIX commands.
- [hitchkey](https://github.com/hitchdev/hitchkey) - python project command runner and invoker that sets up its own virtualenv and working directories.
- [prettystack](https://github.com/crdoconnor/prettystack) - display pretty stacktraces in python.

Build tools that will be documented soons:

- [hitchbuildpy](https://github.com/hitchdev/hitchbuildpy) - tool to precisely build virtualenvs from specified versions of python (bundles pyenv).
- [hitchbuildpg](https://github.com/hitchdev/hitchbuildpg) - tool to precisely build development/testing postgres databases from scratch (installs postgres itself).
- [hitchbuild](https://github.com/hitchdev/hitchbuild) - generic build tool used as a basis for above libraries.
