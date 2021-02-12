.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7e6844c6260242dd39b44d162e06aeb7

Reads all attributes from the file system.

This is useful when information about the file system is collected in a worker thread, and then passed to the UI in the form of caching :sip:ref:`~PyQt6.QtCore.QFileInfo` instances.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.setCaching`, :sip:ref:`~PyQt6.QtCore.QFileInfo.refresh`.
