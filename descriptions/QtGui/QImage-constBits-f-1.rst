.. sip:method-description::
    :status: todo
    :pysig: 9daeab2db5574297592cfe242f3e4da3
    :realsig: () const
    :digest: b5ab848fceb6050fe48f07c1de6ee2fd

Returns a pointer to the first pixel data.

Note that :sip:ref:`~PyQt6.QtGui.QImage` uses `implicit data sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_, but this function does *not* perform a deep copy of the shared pixel data, because the returned data is const.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.bits`, :sip:ref:`~PyQt6.QtGui.QImage.constScanLine`.
