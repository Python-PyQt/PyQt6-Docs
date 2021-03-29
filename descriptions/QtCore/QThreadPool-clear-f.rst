.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e1dc568a34847cc589e0cf9b63441217

Removes the runnables that are not yet started from the queue. The runnables for which :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete` returns ``true`` are deleted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThreadPool.start`.
