.. sip:method-description::
    :status: todo
    :pysig: f66b8fe5c9a42a71784b0410e54eafff
    :realsig: (QThread*)
    :digest: 3f04732ed596c28c06c093a9fd1a868e

Changes the thread affinity for this object and its children. The object cannot be moved if it has a parent. Event processing will continue in the *targetThread*.

To move an object to the main thread, use QApplication::instance() to retrieve a pointer to the current application, and then use QApplication::thread() to retrieve the thread in which the application lives. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 139-139

If *targetThread* is ``nullptr``, all event processing for this object and its children stops, as they are no longer associated with any thread.

Note that all active timers for the object will be reset. The timers are first stopped in the current thread and restarted (with the same interval) in the *targetThread*. As a result, constantly moving an object between threads can postpone timer events indefinitely.

A :sip:ref:`~PyQt6.QtCore.QEvent.Type.ThreadChange` event is sent to this object just before the thread affinity is changed. You can handle this event to perform any special processing. Note that any new events that are posted to this object will be handled in the *targetThread*, provided it is not ``nullptr``: when it is ``nullptr``, no event processing for this object or its children can happen, as they are no longer associated with any thread.

**Warning:** This function is *not* thread-safe; the current thread must be same as the current thread affinity. In other words, this function can only "push" an object from the current thread to another thread, it cannot "pull" an object from any arbitrary thread to the current thread. There is one exception to this rule however: objects with no thread affinity can be "pulled" to the current thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.thread`.
