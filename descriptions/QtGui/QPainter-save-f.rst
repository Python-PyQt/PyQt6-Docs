.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8dfe0a43cf6f2a75c2b4d1a0fcc57f6e

Saves the current painter state (pushes the state onto a stack). A save() must be followed by a corresponding :sip:ref:`~PyQt6.QtGui.QPainter.restore`; the :sip:ref:`~PyQt6.QtGui.QPainter.end` function unwinds the stack.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.restore`.
