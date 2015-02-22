Chapter 1
=========

This chapter will cover the basic scaffolding for a Pygame game. We'll cover:
 * The basic structure of a Pygame program
 * Displaying a window on the screen
 * Some simple drawing primitives

By the end of this chapter you will have a simple program that displays a greeting; a "hello world" program if you will. This chapter is fundamental to the other chapters so please make sure you understand it before moving on to the other chapters.

The structure of a Pygame program
---------------------------------

Take a look at the following program:

.. literalinclude:: program1.py
    :language: python
    :linenos:

Enter this program (or copy it) and run it using ``python program1.py``. You should see a window 800x600 pixels in size quickly appear and disappear. If you miss it try running it again.

Let's break down the program.

.. literalinclude:: program1.py
    :language: python
    :lines: 1-4
    :linenos:

Line 1 tells Unix-basesd systems to search the environment path for a Python interpreter.

Line 2 imports the Python system library (which we'll use to exit the program, along with pygame.quit()).

Line 3 imports the Pygame library.

Line 4 brings in the Rect constant from the locals module. We'll cover this in more detail in a bit.

.. literalinclude:: program1.py
    :language: python
    :lines: 6
    :lineno-start: 6
    :linenos:

Line 6 creates a constant called SCREENRECT which contains a Pygame Rect object (short for "rectangle"). The coordinates for the Pygame Rect object start from the top left corner (0,0) and extend to the bottom right corner (800 pixels across, 600 pixels down, or 800x600). This will be used later to set up the dimensions of our screen for display in lines 8 and 9.

.. literalinclude:: program1.py
    :language: python
    :lines: 8-9
    :lineno-start: 8
    :linenos:

Line 8 defines the main function for our Pygame program. This will be called on line 12 if we're running from the command line (which we are).

Line 9 does the heavy lifting for our current Pygame program. It first determines the size of SCREENRECT (which returns a tuple of (800, 600) and then uses that to set the dimensions for our display. There's more options that we'll cover later on but for now it's enough to know that the default mode for the display is to create a window of a certain dimension (in this case 800x600).

Once the display is created there's nothing to keep it running so the function returns.

.. literalinclude:: program1.py
    :language: python
    :lines: 11-14
    :lineno-start: 11
    :linenos:

Line 11 is a convention in Python to determine if the program is called from the command-line. Essentially it checks to see if the ``__name__`` value has been set to "__main__", which will happen whenever the module we've created is being run as the main program. For now it's enough to know that this will always be true and will then continue running the code below (Lines 12-14). Line 12 calls the ``main`` function (Line 8) and proceeds to set up the display. Once the display is created there's nothing keeping Pygame from continually refreshing that display so it then closes the display and exits the ``main`` function. ``pygame.quit()`` on line 13 cleans up any extraneous Pygame variables and ``sys.exit()`` causes the program to terminate (Note: ``sys.exit()`` is completely optional here as the program will end after executing the last statement on Line 13.)

Well, there you have it. Your first Pygame program. Not nearly as exciting as you expected, right? Likel most scaffolding this program is only a taste of the final shape of your program. We'll make things more interesting in the next section.

The quick "Hello World"
-----------------------

The code in the last section is the basic framework but it doesn't do a whole lot. In this section we'll create a program to display a simple greeting.

.. literalinclude:: program2.py
    :language: python
    :linenos:

Let's go through this and see what we've added:

.. literalinclude:: program2.py
    :language: python
    :lines: 1-5
    :lineno-start: 1
    :linenos:

These lines should look very familiar from program 1 with the exception of ``from time import sleep``. Sleep is a function that we'll use later in the program to pause the program for a few seconds.

.. literalinclude:: program2.py
    :language: python
    :lines: 7-7
    :lineno-start: 7
    :linenos:

We still have SCREENRECT defining a Pygame Rect constant. Again, we'll cover this in a bit.

.. literalinclude:: program2.py
    :language: python
    :lines: 8-10
    :lineno-start: 8
    :linenos:

These lines define several constants using Python tuples. The tuples have three values representing the colors we want. The values in these tuples represent "red", "green" and "blue" values. (There's a fourth value, "alpha" which we'll cover later on). These values give us a "cosmic" shade of purpleish maroon which we'll use for the background color. The Line color is a similar tuple that represents a gray color. (Feel free to substitute these with colors of your choosing.) Lastly we pick a width for our lines.

.. literalinclude:: program2.py
    :language: python
    :lines: 12-14
    :lineno-start: 12
    :linenos:

Lines 12 and 13 are the same lines we used in program1. Line 14 sets the title for the window to "Hi". Since we're doing a simple greeting it makes sense to name the window to match our simple greeting. If we didn't set this our window would show up with the default window title (which on this machine defaults to "pygame window"). 

.. literalinclude:: program2.py
    :language: python
    :lines: 16-16
    :lineno-start: 16 
    :linenos:

Line 16 takes the color set in BACKGROUND_COLOR (which is the "cosmic" shade we mentioned earlier) and fills the background with that color. Fill will take the specified color and draw it into a surface. In this case our surface is the screen itself which was returned with the ``pygame.display.set_mode`` command. 

.. literalinclude:: program2.py
    :language: python
    :lines: 18-21
    :lineno-start:  18
    :linenos:

This section uses the ``pygame.draw.line`` method for drawing a line on the surface. First we give it the target surface to draw on (``surface`` in this instance), and the X, Y coordinates. If you aren't familiar with screen coordinates we'll cover those in a separate section. For now imagine each ``pygame.draw.line`` command is drawing a line given an initial X, Y coordinate. In the case of line 19 we start from the top left of the window, position our cursor 60 pixels to the right and 60 pixels down, and draw down an additional 60 pixels (Y position 120). We do this with the grayish color in LINE_COLOR, and with a line width stored in WIDTH (in this case 5). We repeat the process, moving right 100 pixels from the top left of the screen, and once again draw a line 60 pixels down. That forms the two vertical lines for our "H". Line 21 draws the horizontal line (though not perfectly horizontal, as ``pygame.draw.line`` can draw lines between any two points) and this completes our "H".

.. literalinclude:: program2.py
    :language: python
    :lines: 23-24
    :lineno-start:  23
    :linenos:

We then draw a single line for our "I".

.. literalinclude:: program2.py
    :language: python
    :lines: 26-28
    :lineno-start:  26
    :linenos:

These lines finish off with two lines representing the exclamation point. Note that the "period" for the exclamation point is five pixels down and five pixels wide. In essence this is one way to draw a square. We could have used a rectangle instead but for now this will suffice.

.. literalinclude:: program2.py
    :language: python
    :lines: 30-31
    :lineno-start: 30
    :linenos:

Once we have our drawing in place we call ``pygame.display.update``. Up until this point we haven't actually drawn anything in the window; it's all been in a buffer that Pygame keeps off-screen. By calling ``pygame.display.update`` Pygame will take the contents of that buffer and draw them onto the screen.

Why draw to the buffer instead of the directly on the screen? There are a few reasons but the simplest reason is because we can completely draw our frame prior to displaying it. If we didn't do that we could potentially see the lines being drawn onto the screen. While this might be somewhat artistic in this case it can pose problems for scenes with lots of drawing, and can introduce a "flickering" effect where the scene starts to redraw before our eye has had a chance to see the image. Pygame handles the buffering behind the scenes so there's no good way to show you this effect with Pygame but trust me - it's not pretty.

Line 31 will pause for 5 seconds before returning from the ``main`` method. You'll note that you won't be able to close the window until the 5 seconds elapse. We'll cover how to quit a window without waiting or killing the process in the next section.

The rest of the program is the same as program1.

Run the program and gaze at the wonderfully succinct greeting. But it's not terribly interactive is it? Games aren't much without interactivity, and in the next section we'll cover getting keyboard events to influence the program.

Interactivity
-------------

Interactivity is one of the pillars of any game. Games aren't much fun of you aren't allowed to interact and affect the outcome of the game. Let's make the previous program more interactive by allowing the user to move the greeting around the screen.

Pygame Events
~~~~~~~~~~~~~

We'll cover more of the Pygame event handling in a later section, but I wanted to give you a cursory understanding of how events work in a game how Pygame handles them.

Using the Pygame framework allows you to use the Pygame Event Queue. This is a queue that gives the program access to events in the queue and allows you to post events to the queue. Pygame ships with the ability to capture certain hardwre events (keyboard, mouse, joystick, etc.) and also has the ability to set timed events, which are handy for moving enemies, updating a countdown timer, or other game-related tasks.


