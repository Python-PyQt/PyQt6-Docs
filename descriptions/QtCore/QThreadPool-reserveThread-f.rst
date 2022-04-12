.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: cdac6783cc6540d278fb385eb0b210c5

Reserves one thread, disregarding :sip:ref:`~PyQt6.QtCore.QThreadPool.activeThreadCount` and :sip:ref:`~PyQt6.QtCore.QThreadPool.maxThreadCount`.

Once you are done with the thread, call :sip:ref:`~PyQt6.QtCore.QThreadPool.releaseThread` to allow it to be reused.

**Note:** Even if reserving :sip:ref:`~PyQt6.QtCore.QThreadPool.maxThreadCount` threads or more, the thread pool will still allow a minimum of one thread.

**Note:** This function will increase the reported number of active threads. This means that by using this function, it is possible for :sip:ref:`~PyQt6.QtCore.QThreadPool.activeThreadCount` to return a value greater than :sip:ref:`~PyQt6.QtCore.QThreadPool.maxThreadCount` .

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThreadPool.releaseThread`.
