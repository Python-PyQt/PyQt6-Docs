.. sip:enum-description::
    :status: todo
    :digest: c3a2361b7885e0fab3b68756c7e6765c

This enum describes attributes that change the behavior of application-wide features. These are enabled and disabled using QCoreApplication::setAttribute(), and can be tested for with QCoreApplication::testAttribute().

When this attribute is true Qt will not do the remapping, and pressing the Command modifier will result in :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.MetaModifier`, while pressing the Control modifier will result in :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.ControlModifier`.

Note that the :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey` sequences will always be based on the same modifier (i.e., :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.Copy` will be Command+C regardless of the value set), but what is output for :sip:ref:`~PyQt6.QtGui.QKeySequence.toString` will be different.
