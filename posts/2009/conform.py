#!/usr/bin/env python2

# A little application to visualize a particular class of fractional
# linear transforms on the complex numbers.
#
# You will need to install Python.
# Once Python is installed, save this file to your Desktop and
# double-click on it to run the application.
#
# Apparently Tk does not like drawing big circles, so it can be a
# little glitchy.

########################################################################

# The MIT License
#
# Copyright (c) 2009 Simon Parent
#
# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in
# the Software without restriction, including without
# limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from cmath import *

# Centre of the circle going through z1, z2, z3.
def det3(((a, b, c), (d, e, f), (g, h, i))):
  return a*e*i - a*f*h - b*d*i + b*f*g + c*d*h - c*e*g
def centre(z1, z2, z3):
  z1 += 0j;  z2 += 0j;  z3 += 0j
  M11 = det3([(z.real,    z.imag, 1) for z in (z1, z2, z3)])
  M12 = det3([(abs(z)**2, z.imag, 1) for z in (z1, z2, z3)])
  M13 = det3([(abs(z)**2, z.real, 1) for z in (z1, z2, z3)])
  return 0.5*M12/M11 - 0.5j*M13/M11
# Centre and radius of the circle going through z1, z2, z3.
def circle(z1, z2, z3):
  z1 += 0j;  z2 += 0j;  z3 += 0j
  c = centre(z1, z2, z3)
  return (c, abs(z1 - c))

# Our C1s, circles going through a and b.
# The parameter t is a nonnegative real number.
def c1(t):
  t += 0.0
  return -1, t*1j, 1
c1basis = [1.2, 1.5, 2, 3]
c1basis += [1.0/t for t in c1basis]
c1basis += [1, 0]
c1basis = [c1(t) for t in c1basis]
# Our C2s, circles s.t. |z-a|/|z-b| = t.
# The parameter t is a positive real number.
def c2(t):
  t += 0.0
  if abs(t-1) < 1e-9:
    return -1j, 0.0, 1j
  elif t > 1:
    return tuple([-z for z in c2(1/t)])
  else:
    return (t-1)/(t+1), (t+1)/(t-1), -1+1j*abs(sqrt((4*t*t)/(1-t*t)))
c2basis = [1.2, 1.5, 2, 3]
c2basis += [1.0/t for t in c2basis]
c2basis += [1]
c2basis = [c2(t) for t in c2basis]

# Our map is w = Tz where
# w+1     z+1
# --- = k ---
# w-1     z-1
def Tr(k, z):
  k += 0j;  z += 0j;
  a = ((z-1) + k*(z+1))
  b = ((1-z) + k*(z+1))
  if b == 0:
    return 'infinity' # TODO?
  else:
    return a / b
def T(k, c):
  return tuple([Tr(k, z) for z in c])

########################################################################

# Drawing on a canvas.
def scale(canvas, z):
  w, h = canvas.winfo_width(), canvas.winfo_height()
  s = min(w, h) / 4
  return s*z.conjugate()+(w/2)+(h/2)*1j
def invscale(canvas, z):
  w, h = canvas.winfo_width(), canvas.winfo_height()
  s = min(w, h) / 4
  return ((z-(w/2)-(h/2)*1j)/s).conjugate()
def draw_pt(canvas, p):
  p = scale(canvas, p)
  w1 = p - 3*(1+1j)
  w2 = p + 3*(1+1j)
  canvas.create_oval(w1.real, w1.imag, w2.real, w2.imag, fill = 'black')
def draw_circle(canvas, c):
  # This behaves badly in some boundary cases, oh well.
  z1, z2, z3 = tuple([z+0j for z in c])
  if abs(((z1-z3)/(z2-z3)).imag) < 1e-4:
    w1 = scale(canvas, z1 + (z2-z1) * -100)
    w2 = scale(canvas, z1 + (z2-z1) *  100)
    canvas.create_line(w1.real, w1.imag, w2.real, w2.imag)
  else:
    c, r = circle(z1, z2, z3)
    w1 = scale(canvas, c - r*(1+1j))
    w2 = scale(canvas, c + r*(1+1j))
    canvas.create_oval(w1.real, w1.imag, w2.real, w2.imag)

# Root window.
from Tkinter import *
root = Tk()
root.title("Conform!")
for j in range(2):
  root.grid_columnconfigure(j, weight = 1)
for j in range(5):
  if j < 3:
    root.grid_rowconfigure(j, weight = 0)
  else:
    root.grid_rowconfigure(j, weight = 1)

# Help text.
s='We are considering w = Tz, such that (w+1)/(w-1) = k * (z+1)/(z-1).'
s += '\nPress R to reset to the identity map.  Press Q to quit.'
s += '\nLeft-click to mark a point.  Right-click to clear it.'
label = Label(root, text = s, font = ("Helvetica", 10, "bold"))
label.grid(sticky = NW+SE, column = 0, row = 0, columnspan = 2)

# Sliders.
klog = Scale(root, label = 'log |k|', orient = HORIZONTAL,
            from_ = -4, to = 4, resolution = 0.01)
klog.grid(sticky = NW+SE, column = 0, row = 1, columnspan = 2)
klog.config(command = lambda ignored: draw())
karg = Scale(root, label = 'arg k', orient = HORIZONTAL,
            from_ = -3.14, to = 3.14, resolution = 0.01)
karg.grid(sticky = NW+SE, column = 0, row = 2, columnspan = 2)
karg.config(command = lambda ignored: draw())

# Canvases.
canvases = [None] * 4
for j in range(4):
  c = Canvas(root, width = 300, height = 300,
    borderwidth = 0, highlightthickness = 0)
  c.grid(sticky = NW+SE, column = j%2, row = j/2 + 3)
  canvases[j] = c

# Clicking to mark a point.
pt = None
def click(id, ev):
  global pt
  pt = invscale(canvases[id], ev.x+ev.y*1j)
  if id == 1 or id == 3:
    k = exp(klog.get() + karg.get() * 1j)
    pt = Tr(1.0/k, pt)
  draw()
def rclick():
  global pt
  pt = None
  draw()
for j in range(4):
  canvases[j].bind('<Button-1>', lambda ev, k=j: click(k, ev))
  canvases[j].bind('<Button-3>', lambda ev: rclick())

# Quit and reset keys.
def reset(ignored):
  klog.set(0)
  karg.set(0)
root.bind_all('<r>', reset)
def quit(ignored):
  exit(0)
root.bind_all('<q>', quit)

# Draw command.
def draw():
  k = exp(klog.get() + karg.get() * 1j)
  for canvas in canvases:
    canvas.delete(ALL)
  for j in range(4):
    canvases[j].create_text((0, 0), anchor = 'nw',
        text = ['C1', 'T(C1)', 'C2', 'T(C2)'][j])
  for c in c1basis:
    draw_circle(canvases[0], c)
  for c in c1basis:
    draw_circle(canvases[1], T(k, c))
  for c in c2basis:
    draw_circle(canvases[2], c)
  for c in c2basis:
    draw_circle(canvases[3], T(k, c))
  if pt:
    draw_pt(canvases[0], pt)
    draw_pt(canvases[1], Tr(k, pt))
    draw_pt(canvases[2], pt)
    draw_pt(canvases[3], Tr(k, pt))
  for j in range(4):
    c = canvases[j]
    w, h = int(c.winfo_width()), int(c.winfo_height())
    if j % 2 == 0:
      c.create_line(w-1, 0,   w-1, h)
    if j / 2 == 0:
      c.create_line(0,   h-1, w,   h-1)
root.bind('<Configure>', lambda ignored: draw())

# Go!
root.mainloop()
