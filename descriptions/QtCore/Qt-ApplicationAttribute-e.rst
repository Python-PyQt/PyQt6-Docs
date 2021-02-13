.. sip:enum-description::
    :status: todo
    :digest: b6e5e362f09e519f8388873df566ec09

This enum describes attributes that change the behavior of application-wide features. These are enabled and disabled using :sip:ref:`~PyQt6.QtCore.QCoreApplication.setAttribute`, and can be tested for with :sip:ref:`~PyQt6.QtCore.QCoreApplication.testAttribute`.

When this attribute is true Qt will not do the remapping, and pressing the Command modifier will result in :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers.MetaModifier`, while pressing the Control modifier will result in :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers.ControlModifier`.

Note that the :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey` sequences will always be based on the same modifier (i.e., :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.Copy` will be Command+C regardless of the value set), but what is output for :sip:ref:`~PyQt6.QtGui.QKeySequence.toString` will be different.
