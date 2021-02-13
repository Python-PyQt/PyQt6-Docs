.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: c0152059a259349bc2f01be0d7be8bad

If the currently assigned device is a :sip:ref:`~PyQt6.QtCore.QFile`, or if :sip:ref:`~PyQt6.QtGui.QImageWriter.setFileName` has been called, this function returns the name of the file :sip:ref:`~PyQt6.QtGui.QImageWriter` writes to. Otherwise (i.e., if no device has been assigned or the device is not a :sip:ref:`~PyQt6.QtCore.QFile`), an empty QString is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.setFileName`, :sip:ref:`~PyQt6.QtGui.QImageWriter.setDevice`.
