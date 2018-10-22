---
title: Contributing to Hitch Libraries
---

Thanks for getting involved!

Hitch libraries are developed and tested with the hitch framework. It
probably won't be familiar to you, but it should have [a number of
other advantages](../../principles/hitchdev) that other testing/specification frameworks
don't, including automated dev environment setup.

Below is a step by step guide to get started:

## Mac set up prerequisites

To run integration tests / environment on a Mac, you need to first ensure that [brew](https://brew.sh/) is installed (note that this will require XCode from the Mac App store is installed, and, subsequently, that "xcode-select --install" is run).

Once brew is installed, at a minimum you will need to install python and python3:

```bash
$ brew install python python3
```

Followed by:

```
$ sudo pip install --upgrade hitchkey virtualenv
```

Note that hitchkey is a bootstrap script with zero dependencies and will not interfere with other software.

If you are morally opposed to using "sudo pip install", try using [pipsi](https://github.com/mitsuhiko/pipsi) instead, i.e.:

```
$ pipsi install hitchkey
```

Git clone the repository somewhere new (e.g. a temporary directory) and switch to the branch you want.

Then, run hk in any folder inside the repo:

```bash
$ hk
```

It should install some packages and then output something similar to what you see below.

{{< warning title="Please raise a bug if you see any issues" >}}
Please, if you experience *any* issues with the above steps, [raise a ticket here](https://github.com/hitchdev/hitchstory/issues/new) and describe what happened.

This is vitally important to the health and future development of the framework.
{{< /warning >}}


## Linux set up prerequisites

To set up:

```bash
$ sudo apt-get install python3 python-pip python-virtualenv

$ sudo pip install --upgrade hitchkey
```

Note that hitchkey is a bootstrap script with zero dependencies and will not interfere with other software.

If you are morally opposed to doing "sudo pip install", try using [pipsi](https://github.com/mitsuhiko/pipsi) instead, i.e.:

```
$ pipsi install hitchkey
```

{{< warning title="Please raise a bug if you see any issues" >}}
Please, if you experience *any* issues with the above steps, [raise a ticket here](https://github.com/hitchdev/hitchstory/issues/new) and describe what happened.

This is vitally important to the health and future development of the framework.
{{< /warning >}}

## Using hitchkey

You should be presented with a list of available commands similar to this:

```
Usage: hk command [args]

          bdd - Run story matching keywords.
       docgen - Build documentation.
     doctests - Run doctests in utils.py in python 2 and 3.
         rbdd - Run story matching keywords and rewrite story if code changed.
    readmegen - Build documentation.
   regression - Run regression testing - lint and then run all tests.
         lint - Lint project code and hitch code.
       deploy - Deploy to pypi as specified version.
```

The only commands you really need to worry about (at least initially) are "hk bdd" and "hk regression".

* To regression test the application, run "hk regression". Please run this as a smoke test before writing any code and [raise a ticket](https://github.com/hitchdev/hitchstory/issues/new) if it fails for *any* reason with details.

* To run an *individual* test run "hk bdd keyword" where the keyword or keywords are case insensitive words or *parts* of words that appear in the names of stories. For example, "hk bdd dirty" will run [this story](https://github.com/crdoconnor/strictyaml/blob/master/hitch/dirty-load.story) and "hk bdd exception" will run the exception variation story listed here [the exception variation story here](https://github.com/crdoconnor/strictyaml/blob/master/hitch/dirty-load.story).

If you have gotten this far, congratulations, you're ready to write and run tests!

## Further reading

TODO:

* Writing good, DRY, executable specifications
* 
