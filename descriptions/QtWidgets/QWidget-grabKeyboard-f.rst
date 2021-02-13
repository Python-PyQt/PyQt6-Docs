.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 598a7cba8f321e5a96daf4ccb7f6f978

Grabs the keyboard input.

This widget receives all keyboard events until :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseKeyboard` is called; other widgets get no keyboard events at all. Mouse events are not affected. Use :sip:ref:`~PyQt6.QtWidgets.QWidget.grabMouse` if you want to grab that.

The focus widget is not affected, except that it doesn't receive any keyboard events. :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus` moves the focus as usual, but the new focus widget receives keyboard events only after :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseKeyboard` is called.

If a different widget is currently grabbing keyboard input, that widget's grab is released first.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseKeyboard`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabMouse`, :sip:ref:`~PyQt6.QtWidgets.QWidget.releaseMouse`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusWidget`.
