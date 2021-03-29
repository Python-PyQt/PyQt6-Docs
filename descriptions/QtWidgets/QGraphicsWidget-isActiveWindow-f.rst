.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: a6554e20f915079ab2978d3e655df440

Returns ``true`` if this widget's window is in the active window, or if the widget does not have a window but is in an active scene (i.e., a scene that currently has focus).

The active window is the window that either contains a child widget that currently has input focus, or that itself has input focus.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.activeWindow`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setActiveWindow`, isActive().
