.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: a0ed29d2308e1347fc22164f2d38d408

Returns the position of the window on the desktop excluding any window frame

**Note:** Not all windowing systems support setting or querying top level window positions. On such a system, programmatically moving windows may not have any effect, and artificial values may be returned for the current positions, such as ``QPoint(0, 0)``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setPosition`.
