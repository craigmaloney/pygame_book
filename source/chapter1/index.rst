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

We'll cover more of the Pygame event handling when we build a full game in the next section, but I wanted to give you a brief overview of how Pygame handles events.

Using the Pygame framework allows you to use the Pygame Event Queue. This is a queue that gives the program access to events in the queue and allows you to post events to the queue. Pygame ships with the ability to capture certain hardwre events (keyboard, mouse, joystick, etc.) and also has the ability to set timed events, which are handy for moving enemies, updating a countdown timer, or other game-related tasks.

.. literalinclude:: program3.py
    :language: python
    :lines: 1-94
    :lineno-start: 1
    :linenos:

By adding event code we doubled the amount of code, but we also added a few things:

 * Movement via arrow keys
 * The ability to close the window (without the event code it was impossible to close the window without killing the application
 * The ability to close the window using the Q or the Escape key

.. literalinclude:: program3.py
    :language: python
    :lines: 1-14
    :lineno-start: 1
    :linenos:

The includes in lines 1-5 should look familiar. Lines 6-14 are new though. Let's go through them in turn:

.. literalinclude:: program3.py
    :language: python
    :lines: 6-7
    :lineno-start: 6
    :linenos:

The first event constant imported is KEYDOWN, which is the code Pygame sends when a key is pressed down. We use this event in conjunction with other keyboard events to determine if a key is currently being pressed.

.. literalinclude:: program3.py
    :language: python
    :lines: 8
    :lineno-start: 8
    :linenos:

QUIT is a special event. This is the event Pygame sends when the window is closed by the window manager or operating system. Without this event our program will be unable to terminate properly when the operating system says "please close" and will need extraordinary measures to kill the process (``kill -9`` in the case of a UNIX-like machine).

.. literalinclude:: program3.py
    :language: python
    :lines: 9-14
    :lineno-start: 9
    :linenos:

K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, and K_q all map to the cursor keys, the Escape Key, and the Q key on the computer keyboard. Pygame will submit theese keyboard constants to the event queue when the corresponding key is pressed. If we wanted to use different keys (the standard WASD keys of a first person shooter, perhaps) we'd need to import those key events here.

A large number of Pygame programs found on the Internet use ``from pygame.constants import *`` instead of an explicit import of constants. I've chosen to import these constants explicitly as a matter of style (my editor checks imports and will complain if it sees ``import *``). Explicit imports are a better practice than implicit imports, but feel free to use whatever makes your code easier to read for you.

.. literalinclude:: program3.py
    :language: python
    :lines: 16-20
    :lineno-start: 16
    :linenos:

These are some helpful constants we'll use throughout the rest of the program.

.. literalinclude:: program3.py
    :language: python
    :lines: 22-28
    :lineno-start: 22
    :linenos:

We start the program with our standard ``pygame.display.set_mode`` to set the display. We'll also set the caption (or "title) for our **hello world** program to "Hello World". 

Line 25 sets the keyboard so it will repeat after one millisecond, and every millisecond thereafter while the key is depressed. 

Lines 26-27 set the offset variables to the default constants (currently 60). Line 28 sets a `running` flag which should remain true until we quit the program.

.. literalinclude:: program3.py
    :language: python
    :lines: 30-32
    :lineno-start: 30
    :linenos:

Line 30 continues running the program until `running` is set to `False`. 

Line 32 replaces the background with the BACKGROUND_COLOR.

.. literalinclude:: program3.py
    :language: python
    :lines: 33-50
    :lineno-start: 33
    :linenos:

Here's where the program starts to get interesting. We'll use the `line` method from the Pygame `draw` module. The first argument of the `drawi.line`  method is the surface we'll be drawing on. The next argument is the color of the line that we'll be drawing (stored in the constant `LINE_COLOR`.  The next two arguments are the beginning and end-points of our line, given as Python Tuples. We use `offset_x` and `offset_y` for the origin (which starts off at 60 pixels from the top left corner of the surface and 60 pixels down from the top left of the surface) and then draw a line 60 additional pixels down. The last argument determines the width of the line, which is five pixels in width.

Lines 40 through 50 draw two additional lines, which complete the rest of the letter "H".

.. literalinclude:: program3.py
    :language: python
    :lines: 52-72
    :lineno-start: 52
    :linenos:

Lines 52-72 draw the rest of our greeting ("I" and "!"). Note how each of the coordinates reference `offset_x` and `offset_y`. Why we chose to use those as variables will become apparent in the next section.

Pygame Keyboard Events and the Event Queue
------------------------------------------

Interactivity is key to any game and the next section of code takes our program from a program that simply displays "HI!" and transforms it into an interactive program. The Pygame event queue is central to all of the games in this book so we'll take a closer look at how to take the events that are in the event queue and process them to make our "HI!" move around the screen.

The Pygame event queue is a queue created when a Pygame program is instantiated. The queue contains a combination of keyboard, joystick, window-manager, and other events and presents them in a way that our Pygame code can use. The ``pygame.event.get()`` call will pop the events off of the event queue. The events are in the form of a list, which we can then iterate over. Like most queues there is a finite number of events that can be stored in the queue so it's critical to continually poll the queue. Running the ``.get()`` method will pull off all of the events waiting in the queue. It's a good idea to poll ths queue throughout the execution of the code lest we overflow the queue with events.

There are many different methods for interacting with the queue. We'll discuss more of them later in the book. For now we'll only cover using ``.get()`` to grab all pending events.

Events come in several types. Our program uses the KEYDOWN event, which is an event that fires off when the user presses a key down on the keyboard. We check the event type (KEYDOWN) prior to checking the key value itself. We import the constant "KEYDOWN" from the Pygame constants rather than check the event type against the number KEYDOWN represents (2 as of this writing). It's handy to use the constants rather than trying to remember the numeric representation. 

+----------------+---------------------+
|Event Type      |Additional attributes|
+================+=====================+
|QUIT            |none                 |
+----------------+---------------------+
|ACTIVEEVENT     |gain, state          |
+----------------+---------------------+
|KEYDOWN         |unicode, key, mod    |
+----------------+---------------------+
|KEYUP           |key, mod             |
+----------------+---------------------+
|MOUSEMOTION     |pos, rel, buttons    |
+----------------+---------------------+
|MOUSEBUTTONUP   |pos, button          |
+----------------+---------------------+
|MOUSEBUTTONDOWN |pos, button          |
+----------------+---------------------+
|JOYAXISMOTION   |joy, axis, value     |
+----------------+---------------------+
|JOYBALLMOTION   |joy, ball, rel       |
+----------------+---------------------+
|JOYHATMOTION    |joy, hat, value      |
+----------------+---------------------+
|JOYBUTTONUP     |joy, button          |
+----------------+---------------------+
|JOYBUTTONDOWN   |joy, button          |
+----------------+---------------------+
|VIDEORESIZE     |size, w, h           |
+----------------+---------------------+
|VIDEOEXPOSE     |none                 |
+----------------+---------------------+
|USEREVENT       |code                 |
+----------------+---------------------+

We'll talk about the other event types and how to handle them later in the book but for now this list should give you a good idea of the sorts of events that Pygame handles. Not only are Joysticks, Keyboards, and Mice given events but also events for whether the window was resized or contains focus. There's also a USEREVENT that we'll find useful for triggering other parts of our code.

Let's step through the code itself to see what is happening:

.. literalinclude:: program3.py
    :language: python
    :lines: 74-87
    :lineno-start: 74
    :linenos:

Line 74 copies the events that are waiting in the pygame event queue since the last time the events were picked up. The event queue holds all of the events since the program was initialized, and continues receiving events for as long as the application is running. The ``events`` variable stores the list of those events for us to process in the upcoming block of code.  
