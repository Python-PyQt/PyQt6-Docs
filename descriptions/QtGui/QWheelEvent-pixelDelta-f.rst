.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: ad095f1b179274c2460e5111d948a6bd

Returns the scrolling distance in pixels on screen. This value is provided on platforms that support high-resolution pixel-based delta values, such as macOS. The value should be used directly to scroll content on screen.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qevent.py
    :lines: 64-77

**Note:** On platforms that support scrolling :sip:ref:`~PyQt6.QtGui.QWheelEvent.phase`, the delta may be null when:

* scrolling is about to begin, but the distance did not yet change (\ :sip:ref:`~PyQt6.QtCore.Qt.ScrollPhase.ScrollBegin`),

* or scrolling has ended and the distance did not change anymore (\ :sip:ref:`~PyQt6.QtCore.Qt.ScrollPhase.ScrollEnd`).

**Note:** On X11 this value is driver specific and unreliable, use :sip:ref:`~PyQt6.QtGui.QWheelEvent.angleDelta` instead
