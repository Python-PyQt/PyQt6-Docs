.. sip:method-description::
    :status: todo
    :pysig: d33117a4cf830e8da8ce315c28395b25
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: 0c18e7ef110b6d41ae59b268352b29d3

Constructs a widget which is a child of *parent*, with widget flags set to *f*.

If *parent* is ``nullptr``, the new widget becomes a window. If *parent* is another widget, this widget becomes a child window inside *parent*. The new widget is deleted when its *parent* is deleted.

The widget flags argument, *f*, is normally 0, but it can be set to customize the frame of a window (i.e. *parent* must be ``nullptr``). To customize the frame, use a value composed from the bitwise OR of any of the window flags.

If you add a child widget to an already visible widget you must explicitly show the child to make it visible.

Note that the X11 version of Qt may not be able to deliver all combinations of style flags on all systems. This is because on X11, Qt can only ask the window manager, and the window manager can override the application's settings. On Windows, Qt can set whatever flags you want.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.windowFlags`.
