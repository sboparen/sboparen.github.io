---
layout: post
title: twotimes
ura_date: 2011-03-06
redirect_from: /posts/2011/twotimes.html
---

There is an infamous qualifier problem used to evaluate the ability
of second-year students to create a complete program by themselves.
This problem is to read in a file consisting of a series of integers,
print out the integers (one per line), and then print them out again.

This is my tongue-in-cheek solution which shows that students using
C are not at a disadvantage, as they do not need a dynamically
resizing data structure to deal with the number of integers being
unknown until the end of the file is reached.

<!--more-->

<a href="twotimes.c">twotimes.c</a>

{% highlight c %}
{% include_relative twotimes.c %}
{% endhighlight %}
