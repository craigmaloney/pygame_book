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

These lines should look very familiar from program 1.

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

Lines 12 and 13 are the same lines we used in program1 but 
