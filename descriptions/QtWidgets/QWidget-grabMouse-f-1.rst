.. sip:method-description::
    :status: todo
    :pysig: 8e918d8b61b1642c2f8119e8dadd3b5a
    :realsig: (const QCursor&)
    :digest: 0e8f618783b5c4e1a62f36ae8b5d2bba

Grabs the mouse input and changes the cursor shape.

The cursor will assume shape *cursor* (for as long as the mouse focus is grabbed) and this widget will be the only one to receive mouse events until :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseMouse` is called().

**Warning:** Grabbing the mouse might lock the terminal.

**Note:** See the note in :sip:ref:`~PyQt6.QtWidgets.QWidget.grabMouse`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseMouse`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabKeyboard`, :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseKeyboard`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setCursor`.
