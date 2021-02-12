.. sip:method-description::
    :status: todo
    :pysig: dfda33981b1b5e20d2d8ab352cd608fb
    :realsig: (QRunnable*)
    :digest: 51d97fedcf6e03dc84797c3c88dc875b

Attempts to remove the specified *runnable* from the queue if it is not yet started. If the runnable had not been started, returns ``true``, and ownership of *runnable* is transferred to the caller (even when ``runnable->autoDelete() == true``). Otherwise returns ``false``.

**Note:** If ``runnable->autoDelete() == true``, this function may remove the wrong runnable. This is known as the `ABA problem <https://en.wikipedia.org/wiki/ABA_problem>`_: the original *runnable* may already have executed and has since been deleted. The memory is re-used for another runnable, which then gets removed instead of the intended one. For this reason, we recommend calling this function only for runnables that are not auto-deleting.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThreadPool.start`, :sip:ref:`~PyQt6.QtCore.QRunnable.autoDelete`.
