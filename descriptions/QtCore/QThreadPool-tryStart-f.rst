.. sip:method-description::
    :status: todo
    :pysig: dfda33981b1b5e20d2d8ab352cd608fb
    :realsig: (QRunnable*)
    :digest: 4a4e93fe5b6532964163cc8e77a7f524

Attempts to reserve a thread to run *runnable*.

If no threads are available at the time of calling, then this function does nothing and returns ``false``. Otherwise, *runnable* is run immediately using one available thread and this function returns ``true``.

Note that on success the thread pool takes ownership of the *runnable* if :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete` returns ``true``, and the *runnable* will be deleted automatically by the thread pool after the :sip:ref:`~PyQt6.QtCore.QRunnable.run` returns. If :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete` returns ``false``, ownership of *runnable* remains with the caller. Note that changing the auto-deletion on *runnable* after calling this function results in undefined behavior.
