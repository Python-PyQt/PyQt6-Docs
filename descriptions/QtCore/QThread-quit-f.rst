.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: dcacb420d16698c1bd71dd0f9a3e6438

Tells the thread's event loop to exit with return code 0 (success). Equivalent to calling :sip:ref:`~PyQt6.QtCore.QThread.exit`\ (0).

This function does nothing if the thread does not have an event loop.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.exit`, :sip:ref:`~PyQt6.QtCore.QEventLoop`.
