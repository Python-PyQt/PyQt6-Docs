.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a19437d6d44ac50175ebefa404a20f97

Grabs the mouse input.

This widget receives all mouse events until :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseMouse` is called; other widgets get no mouse events at all. Keyboard events are not affected. Use :sip:ref:`~PyQt6.QtWidgets.QWidget.grabKeyboard` if you want to grab that.

**Warning:** Bugs in mouse-grabbing applications very often lock the terminal. Use this function with extreme caution, and consider using the ``-nograb`` command line option while debugging.

It is almost never necessary to grab the mouse when using Qt, as Qt grabs and releases it sensibly. In particular, Qt grabs the mouse when a mouse button is pressed and keeps it until the last button is released.

**Note:** Only visible widgets can grab mouse input. If :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible` returns ``false`` for a widget, that widget cannot call .

**Note:** On Windows,  only works when the mouse is inside a window owned by the process. On macOS,  only works when the mouse is inside the frame of that widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseMouse`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabKeyboard`, :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseKeyboard`.
