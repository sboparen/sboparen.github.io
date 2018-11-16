---
layout: post
title: Python Progress
ura_date: 2013-10-24
redirect_from: /posts/2013/progress.html
---

What does this Python program output?

{% highlight python %}
plus = [lambda a: a + b for b in range(10)]
print(plus[2](2))
{% endhighlight %}

<!--more-->

Well, let's try it:

~~~
$ python2 --version
Python 2.7.3
$ python3 --version
Python 3.3.0

$ python2 lambda.py
11
$ python3 lambda.py
11
~~~

Even better is the following program, which shows that some progress
has been made.

<a href="progress.py">progress.py</a>

{% highlight python %}
{% include_relative progress.py %}
{% endhighlight %}
