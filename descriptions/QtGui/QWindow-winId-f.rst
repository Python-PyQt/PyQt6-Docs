.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 1dbcf79ee9d72de08c5217f8739fddc5

Returns the window's platform id.

**Note:** This function will cause the platform window to be created if it is not already. Returns 0, if the platform window creation failed.

For platforms where this id might be useful, the value returned will uniquely represent the window inside the corresponding screen.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.screen`.
