.. sip:method-description::
    :status: todo
    :pysig: d9da5305607fa1793b1c0f02c601211f
    :realsig: (int,int)
    :digest: f1ace69b940cca4dda9630d6f3e6f003

Removes the child item at (\ *row*, *column*) without deleting it, and returns a pointer to the item. If there was no child at the given location, then this function returns ``nullptr``.

Note that this function, unlike :sip:ref:`~PyQt6.QtGui.QStandardItem.takeRow` and :sip:ref:`~PyQt6.QtGui.QStandardItem.takeColumn`, does not affect the dimensions of the child table.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.child`, :sip:ref:`~PyQt6.QtGui.QStandardItem.takeRow`, :sip:ref:`~PyQt6.QtGui.QStandardItem.takeColumn`.
