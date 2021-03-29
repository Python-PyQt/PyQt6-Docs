.. sip:method-description::
    :status: todo
    :pysig: c892221e5d37c603a15a46fc5cc6c726
    :realsig: (QRunnable*,int)
    :digest: 3b4b86415bf24befb417098402a7b053

Reserves a thread and uses it to run *runnable*, unless this thread will make the current thread count exceed :sip:ref:`~PyQt6.QtCore.QThreadPool.maxThreadCount`. In that case, *runnable* is added to a run queue instead. The *priority* argument can be used to control the run queue's order of execution.

Note that the thread pool takes ownership of the *runnable* if :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete` returns ``true``, and the *runnable* will be deleted automatically by the thread pool after the :sip:ref:`~PyQt6.QtCore.QRunnable.run` returns. If :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete` returns ``false``, ownership of *runnable* remains with the caller. Note that changing the auto-deletion on *runnable* after calling this functions results in undefined behavior.
