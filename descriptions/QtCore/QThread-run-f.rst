.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8515dc1755fe50d1352ef6c5a368dd55

The starting point for the thread. After calling :sip:ref:`~PyQt6.QtCore.QThread.start`, the newly created thread calls this function. The default implementation simply calls :sip:ref:`~PyQt6.QtCore.QThread.exec`.

You can reimplement this function to facilitate advanced thread management. Returning from this method will end the execution of the thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.start`, :sip:ref:`~PyQt6.QtCore.QThread.wait`.
