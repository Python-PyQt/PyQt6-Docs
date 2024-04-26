.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0daab5be868ea7c618da589b9e20a574

Grabs the mouse input.

This widget receives all mouse events until :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseMouse` is called; other widgets get no mouse events at all. Keyboard events are not affected. Use :sip:ref:`~PyQt6.QtWidgets.QWidget.grabKeyboard` if you want to grab that.

**Warning:** Bugs in mouse-grabbing applications very often lock the terminal. Use this function with extreme caution, and consider using the ``-nograb`` command line option while debugging.

It is seldom necessary to grab the mouse when using Qt, as Qt grabs and releases it sensibly. In particular, Qt grabs the mouse when a mouse button is pressed and keeps it until the last button is released.

**Note:** Only visible widgets can grab mouse input. If :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible` returns ``false`` for a widget, that widget cannot call grabMouse().

**Note:** On Windows, grabMouse() only works when the mouse is inside a window owned by the process. On macOS, grabMouse() only works when the mouse is inside the frame of that widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseMouse`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabKeyboard`, :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseKeyboard`.
