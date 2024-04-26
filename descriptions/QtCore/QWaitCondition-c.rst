.. sip:class-description::
    :status: todo
    :brief: Condition variable for synchronizing threads
    :digest: 13bdaf0f23e7ccce65308d3ce8d970dc

The :sip:ref:`~PyQt6.QtCore.QWaitCondition` class provides a condition variable for synchronizing threads.

:sip:ref:`~PyQt6.QtCore.QWaitCondition` allows a thread to tell other threads that some sort of condition has been met. One or many threads can block waiting for a :sip:ref:`~PyQt6.QtCore.QWaitCondition` to set a condition with :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeOne` or :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeAll`. Use :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeOne` to wake one randomly selected thread or :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeAll` to wake them all.

For example, let's suppose that we have three tasks that should be performed whenever the user presses a key. Each task could be split into a thread, each of which would have a :sip:ref:`~PyQt6.QtCore.QThread.run` body like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qwaitcondition_unix.py
    :lines: 54-59

Here, the ``keyPressed`` variable is a global variable of type :sip:ref:`~PyQt6.QtCore.QWaitCondition`.

A fourth thread would read key presses and wake the other three threads up every time it receives one, like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qwaitcondition_unix.py
    :lines: 64-67

The order in which the three threads are woken up is undefined. Also, if some of the threads are still in ``do_something()`` when the key is pressed, they won't be woken up (since they're not waiting on the condition variable) and so the task will not be performed for that key press. This issue can be solved using a counter and a :sip:ref:`~PyQt6.QtCore.QMutex` to guard it. For example, here's the new code for the worker threads:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qwaitcondition_unix.py
    :lines: 72-83

Here's the code for the fourth thread:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qwaitcondition_unix.py
    :lines: 88-100

The mutex is necessary because the results of two threads attempting to change the value of the same variable simultaneously are unpredictable.

Wait conditions are a powerful thread synchronization primitive. The `Producer and Consumer using Wait Conditions <https://doc.qt.io/qt-6/qtcore-threads-waitconditions-example.html>`_ example shows how to use :sip:ref:`~PyQt6.QtCore.QWaitCondition` as an alternative to :sip:ref:`~PyQt6.QtCore.QSemaphore` for controlling access to a circular buffer shared by a producer thread and a consumer thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex`, :sip:ref:`~PyQt6.QtCore.QSemaphore`, :sip:ref:`~PyQt6.QtCore.QThread`, `Producer and Consumer using Wait Conditions <https://doc.qt.io/qt-6/qtcore-threads-waitconditions-example.html>`_.
