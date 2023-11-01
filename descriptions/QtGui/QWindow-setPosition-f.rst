.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (const QPoint&)
    :digest: 52c141317bf0671dc641722558d68506

set the position of the window on the desktop to *pt*

The position is in relation to the virtualGeometry() of its screen.

For interactively moving windows, see :sip:ref:`~PyQt6.QtGui.QWindow.startSystemMove`. For interactively resizing windows, see :sip:ref:`~PyQt6.QtGui.QWindow.startSystemResize`.

**Note:** Not all windowing systems support setting or querying top level window positions. On such a system, programmatically moving windows may not have any effect, and artificial values may be returned for the current positions, such as ``QPoint(0, 0)``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.position`, :sip:ref:`~PyQt6.QtGui.QWindow.startSystemMove`.
