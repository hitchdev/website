---
title: The Technical Debt Dial: We don't need better metaphors for technical debt. We need better units of account.
---

Week 41:

[ picture of a bar chart with refactoring / features and bugs ]

There are few developers who have worked in a business that haven't had a conversation
with "the business" that didn't go something like this:

Developer : Remember we need to clean out the reports module and upgrade some of our dependencies.

Product owner : We don't have time for that.

Developer : You said last week that we could do this week.

Product owner : I understand but I just don't think we've got enough time this sprint.

There are several odd things about this dynamic - the developer is, at best,
selling the idea of letting the business allow them to improve the
quality of their software. In theory the *business* should be asking the *developer*
to improve the quality of their software as and when it is needed just as the business
asks a developer to implement a feature.

The other odd thing is that the product owner most likely has no idea how important the
thing they're being "sold" on or its relative importance with all of the other competing
priorities.

A lot of ink has been spilled over this issue. A lot of developers think that
the problem is that the business doesn't really "get" technical debt and thus
develop ever more elaborate metaphors to establish what it means and why it's so
important.

I don't think that's true at all. I think non-techs get the concept easily. What they
don't get is any kind of unit of account, and that's our fault.

They can't see numbers; they can't visualize the issue so they resort to the next
best thing: ignoring it and hoping it goes away.

This isn't completely irrational. Sometimes it doesn't come back to bite them.

In high trust teams this isn't such a huge issue. Developers can say "I need some time
to fix the hacks I made in ticket 155" and the product owner schedules it in.
In turn the product owner trusts the developer will not spend all of their time
rewriting the code in haskell for fun or whatever.

Unfortunately, most of us work in medium or low trust environments, so we need to
figure out a way to deal with this problem.

## Shift technical debt from something developers whine about to something the business controls

I have an internal "tech debt dial" which goes from 0% to 100%.

If I dial it down to 0% that means the team should be in full on hack mode.

Fuck tests, fuck good coding standards - the important thing is just to get it *done*.

If I dial it up to 100% that means the team only works on code quality (refactoring) and/or
tooling (e.g. tests / CI infrastructure).

The developers could split this time any way they want - e.g. if they need to create
entire stories to refactor chunks of code they could do that. Or, they could use part
of the time in a new story to refactor the code related to that story.

Ultimately on a normal day on a normal code base, 30% is a decent place to leave it. In practice on a lot
of projects experienced developers have an internal "sense" that this is about right and they
might dial it up in response to external pressures or dial it down in more relaxed times.

With this, the developers retain full control when and where they engage in refactoring
while 

## Nice idea in theory, but my product owner would leave it at 0% permanently. What's the point?

Many developers are used to the idea that begging for time to refactor code
always falls on deaf ears. Some will give up asking and resign themselves 


I try to communicate to the business representative (product owner/CEO) that:

* This is basically a proxy for the long term quality of your product. If you ask for 0% for 3 months don't be surprised if you get a pile of buggy shit that customers hate: it's what you asked for.

* It can be dialed up and down at will, pretty much at any time, and that the level is completely a business decision.

* Leaving it at 100% or 0% for extended periods is exactly as stupid as it sounds.

* The content of that time ought to be solely a tech decision. They should work on what they think the biggest problems are without having to justify that to anybody why they are doing it (note: this directly contradicts scrum, which says big tooling/refactoring stories get scheduled by the product owner).

* Very low % is actually okay for a short while if there's a good reason (e.g. a non-made up deadline like a trade show) and you dial it back up to compensate later. Hacks that get unwound quickly don't do much damage; hacks that fester do - debt compounds. 20% time now may be equivalent to 40% 6 months from now.

* Very low % on a per project basis is sometimes okay too (some projects get market tested, don't work out and get thrown in the trash. code quality should not be a priority if that is at all likely).

* The % is kind of a rough guideline. The team isn't going to follow it exactly, especially when shit goes down.

## The desired level of quality will vary from team to team and industry to industry

While lots of programmers would prefer to only work on high quality, clean code, the reality is
that most of the market doesn't want that. Shifting consumer tastes and a constantly moving
business landscape means that a great deal of the time the biggest risk to a software product
isn't building the right thing in the wrong way, but building the wrong thing in the right way.

In such markets, especially ones where a winner or several winners take all, sacrificing
product quality in exchange for product speed can be a rational strategy.

It can also make sense for a startup in initial stages that are trying to test if there *is*
a market for their idea before securing money to build it. Conceptually, keeping the dial low
isn't much different to using debt or venture financing to fund a risky venture.

## How do I introduce the dial to my team?

Let's say you're the lowest ranking and least important member (or perhaps the newest)
member of your team and you desperately want to improve the code quality. You know that
if you introduce a new "thing" the team may be resistant (perhaps you tried introducing
them to linting and they demurred) and you want to avoid outright rejection again:

Here's how you do it:

1) Start by measuring - e.g. start a spreadsheet and collate estimates as to % of ticket was refactoring or tooling. This is politically safe - all it requires is asking questions.

2) Ask team members how they feel about the status of the code quality (good/bad/terrible) and the direction (getting better/getting worse/staying the same).

2) Aggregate these values and try to calculate what % of each cadence (sprint/week/whatever) was spent on refactoring.

3) After a few sprints, start graphing, share the graph and start a discussion around the graph (what it means, etc.).

## My team is implicitly at "0%" thanks to all the pressure we're under. I think the manager will leave it at 0%.

What is measured gets improved -- Peter Drucker

Yes. Let's run through a simple scenario to see why:



The primary reason for this is visibility.

Firstly, it might not, but if it doesn't then that signals that the business truly doesn't care about quality.
If they built a product which was experimental then their priority isn't product quality it's testing that
product with customers to see whether it ever needed to be built in the first place. "0%" products aren't
necessarily bad.

In such cases if such work gets you down then really your only option is to leave and work for a company
that does care, maybe in an industry where it will clearly matter.

In practice every company and team will have 





All of the teams I've worked at with shitty coding practices fell in to one of three groups:

    Insulated from market pressures - e.g. government department or massive oligopoly corporation that has exactly zero risk of upstart competitors eating their lunch because they're in an industry with such high barriers to entry.

    Their competitive advantage wasn't based on the quality of their tech - e.g. it's an industry where sales/marketing is mainly what matters not tech quality, tech was a sideshow to a different product, etc. In one case they just battered the competition in court with their patent portfolio.

    On the road to bankruptcy (or at the very least, losing a bunch of money).

