.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: b82d60a63d95f017eefb294e13339dcb

If the currently assigned device is a :sip:ref:`~PyQt6.QtCore.QFile`, or if :sip:ref:`~PyQt6.QtGui.QImageReader.setFileName` has been called, this function returns the name of the file :sip:ref:`~PyQt6.QtGui.QImageReader` reads from. Otherwise (i.e., if no device has been assigned or the device is not a :sip:ref:`~PyQt6.QtCore.QFile`), an empty QString is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.setFileName`, :sip:ref:`~PyQt6.QtGui.QImageReader.setDevice`.
