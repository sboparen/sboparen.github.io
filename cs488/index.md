---
layout: post
title: Highlights from CS 488
date: 2009-07-30
redirect_from: /posts/2009/graphics.html
---

Some images rendered by the programs I wrote while I was taking
[Introduction to Computer Graphics](
https://www.student.cs.uwaterloo.ca/~cs488/).
<!--more-->
Click any image to enlarge.

## Puppet Assignment

We were given the following model as a benchmark to test the
correctness of our transformations.

<a href="a3mark.png">
<img width="400" style="max-width: 100%; display: block;
margin-left: auto; margin-right: auto;"
src="a3mark.png">
</a>

So I decided to bring it to life as my puppet.
I think it turned out pretty cute, but it's definitely challenging
to model with nothing but spheres!

<a href="gnom.png">
<img width="400" style="max-width: 100%; display: block;
margin-left: auto; margin-right: auto;"
src="gnom.png">
</a>

## Raytraced Images

Here I used data from the anti-aliasing pass to make a visualization
of the edges in the image.
The actual scene isn't that exciting, but I thought that this
visualization looked kind of cool.

<a href="ray-edges.png">
<img width="400" style="max-width: 100%; display: block;
margin-left: auto; margin-right: auto;"
src="ray-edges.png">
</a>

As part of the project requirements, we had to render a scene which
used all of the features of our raytracer.
I had fun creating the procedurally generated plants by
using the techniques described in
[The Algorithmic Beauty of Plants](
http://algorithmicbotany.org/papers/#abop).

<a href="ray-finalscene.png">
<img width="400" style="max-width: 100%; display: block;
margin-left: auto; margin-right: auto;"
src="ray-finalscene.png">
</a>

This last one is my favourite.
It really shows off the caustics we can get by using
[photon mapping](http://graphics.ucsd.edu/~henrik/papers/book/).

<a href="ray-waterglass.png">
<img width="400" style="max-width: 100%; display: block;
margin-left: auto; margin-right: auto;"
src="ray-waterglass.png">
</a>
