.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ce5e1d24e253896d479d716fd5f80641

Reserves one thread, disregarding :sip:ref:`~PyQt6.QtCore.QThreadPool.activeThreadCount` and :sip:ref:`~PyQt6.QtCore.QThreadPool.maxThreadCount`.

Once you are done with the thread, call :sip:ref:`~PyQt6.QtCore.QThreadPool.releaseThread` to allow it to be reused.

**Note:** This function will always increase the number of active threads. This means that by using this function, it is possible for :sip:ref:`~PyQt6.QtCore.QThreadPool.activeThreadCount` to return a value greater than :sip:ref:`~PyQt6.QtCore.QThreadPool.maxThreadCount` .

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThreadPool.releaseThread`.
