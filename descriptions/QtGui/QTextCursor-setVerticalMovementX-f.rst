.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 7ab6f6404900713f4c5c765a5d5ebcce

Sets the visual x position for vertical cursor movements to *x*.

The vertical movement x position is cleared automatically when the cursor moves horizontally, and kept unchanged when the cursor moves vertically. The mechanism allows the cursor to move up and down on a visually straight line with proportional fonts, and to gently "jump" over short lines.

A value of -1 indicates no predefined x position. It will then be set automatically the next time the cursor moves up or down.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.verticalMovementX`.
