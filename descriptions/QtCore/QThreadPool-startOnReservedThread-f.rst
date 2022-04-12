.. sip:method-description::
    :status: todo
    :pysig: eb55ccd9d404cc783c5b17229e120279
    :realsig: (QRunnable*)
    :digest: 7fbbb6dd88a6eeb40d70efd9d383b2c2

Releases a thread previously reserved with :sip:ref:`~PyQt6.QtCore.QThreadPool.reserveThread` and uses it to run *runnable*.

Note that the thread pool takes ownership of the *runnable* if :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete` returns ``true``, and the *runnable* will be deleted automatically by the thread pool after the :sip:ref:`~PyQt6.QtCore.QRunnable.run` returns. If :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete` returns ``false``, ownership of *runnable* remains with the caller. Note that changing the auto-deletion on *runnable* after calling this functions results in undefined behavior.

**Note:** Calling this when no threads are reserved results in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThreadPool.reserveThread`, :sip:ref:`~PyQt6.QtCore.QThreadPool.start`.
