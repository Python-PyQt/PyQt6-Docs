.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3e0e5590b5ced2b790ae1318e69e1d56

Releases a thread previously reserved by a call to :sip:ref:`~PyQt6.QtCore.QThreadPool.reserveThread`.

**Note:** Calling this function without previously reserving a thread temporarily increases :sip:ref:`~PyQt6.QtCore.QThreadPool.maxThreadCount`. This is useful when a thread goes to sleep waiting for more work, allowing other threads to continue. Be sure to call :sip:ref:`~PyQt6.QtCore.QThreadPool.reserveThread` when done waiting, so that the thread pool can correctly maintain the :sip:ref:`~PyQt6.QtCore.QThreadPool.activeThreadCount`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThreadPool.reserveThread`.
