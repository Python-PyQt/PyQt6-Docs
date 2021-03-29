.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: 67583765d609edc17072eb80268a3797

Enters the event loop and waits until :sip:ref:`~PyQt6.QtCore.QThread.exit` is called, returning the value that was passed to :sip:ref:`~PyQt6.QtCore.QThread.exit`. The value returned is 0 if :sip:ref:`~PyQt6.QtCore.QThread.exit` is called via :sip:ref:`~PyQt6.QtCore.QThread.quit`.

This function is meant to be called from within :sip:ref:`~PyQt6.QtCore.QThread.run`. It is necessary to call this function to start event handling.

**Note:** This can only be called within the thread itself, i.e. when it is the current thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.quit`, :sip:ref:`~PyQt6.QtCore.QThread.exit`.
