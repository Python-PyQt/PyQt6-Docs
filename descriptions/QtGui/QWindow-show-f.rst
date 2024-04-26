.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c2903a7216089868d38b4985bd7ead9d

Shows the window.

For child windows, this is equivalent to calling :sip:ref:`~PyQt6.QtGui.QWindow.showNormal`. Otherwise, it is equivalent to calling :sip:ref:`~PyQt6.QtGui.QWindow.showFullScreen`, :sip:ref:`~PyQt6.QtGui.QWindow.showMaximized`, or :sip:ref:`~PyQt6.QtGui.QWindow.showNormal`, depending on the platform's default behavior for the window type and flags.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.showFullScreen`, :sip:ref:`~PyQt6.QtGui.QWindow.showMaximized`, :sip:ref:`~PyQt6.QtGui.QWindow.showNormal`, :sip:ref:`~PyQt6.QtGui.QWindow.hide`, :sip:ref:`~PyQt6.QtGui.QStyleHints.showIsFullScreen`, :sip:ref:`~PyQt6.QtGui.QWindow.flags`.
