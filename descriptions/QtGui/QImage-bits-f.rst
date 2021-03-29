.. sip:method-description::
    :status: todo
    :pysig: 49c4e82b5e484f0f98053794b701c0e7
    :realsig: ()
    :digest: 792157525ee28414c0960ed118d65e55

Returns a pointer to the first pixel data. This is equivalent to :sip:ref:`~PyQt6.QtGui.QImage.scanLine`\ (0).

Note that :sip:ref:`~PyQt6.QtGui.QImage` uses `implicit data sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_. This function performs a deep copy of the shared pixel data, thus ensuring that this :sip:ref:`~PyQt6.QtGui.QImage` is the only one using the current return value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.scanLine`, :sip:ref:`~PyQt6.QtGui.QImage.sizeInBytes`, :sip:ref:`~PyQt6.QtGui.QImage.constBits`.
