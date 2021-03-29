.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 7f334cdd425d043cd8a63372c7f3aff4

Returns the name used to create the icon, if available.

Depending on the way the icon was created, it may have an associated name. This is the case for icons created with :sip:ref:`~PyQt6.QtGui.QIcon.fromTheme` or icons using a :sip:ref:`~PyQt6.QtGui.QIconEngine` which supports the QIconEngine::IconNameHook.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.fromTheme`, :sip:ref:`~PyQt6.QtGui.QIconEngine`.
