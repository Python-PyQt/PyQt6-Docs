.. sip:class-description::
    :status: todo
    :brief: Platform-independent way to manage threads
    :digest: 9f36fd40ce5c82a7d23af6ee3afae596

The :sip:ref:`~PyQt6.QtCore.QThread` class provides a platform-independent way to manage threads.

A :sip:ref:`~PyQt6.QtCore.QThread` object manages one thread of control within the program. QThreads begin executing in :sip:ref:`~PyQt6.QtCore.QThread.run`. By default, :sip:ref:`~PyQt6.QtCore.QThread.run` starts the event loop by calling :sip:ref:`~PyQt6.QtCore.QThread.exec` and runs a Qt event loop inside the thread.

You can use worker objects by moving them to the thread using :sip:ref:`~PyQt6.QtCore.QObject.moveToThread`.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qthread.py
    :lines: 80-116

The code inside the Worker's slot would then execute in a separate thread. However, you are free to connect the Worker's slots to any signal, from any object, in any thread. It is safe to connect signals and slots across different threads, thanks to a mechanism called :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection`.

Another way to make code run in a separate thread, is to subclass :sip:ref:`~PyQt6.QtCore.QThread` and reimplement :sip:ref:`~PyQt6.QtCore.QThread.run`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qthread.py
    :lines: 57-75

In that example, the thread will exit after the run function has returned. There will not be any event loop running in the thread unless you call :sip:ref:`~PyQt6.QtCore.QThread.exec`.

It is important to remember that a :sip:ref:`~PyQt6.QtCore.QThread` instance lives in the old thread that instantiated it, not in the new thread that calls :sip:ref:`~PyQt6.QtCore.QThread.run`. This means that all of :sip:ref:`~PyQt6.QtCore.QThread`'s queued slots and :sip:ref:`~PyQt6.QtCore.QMetaObject.invokeMethod` will execute in the old thread. Thus, a developer who wishes to invoke slots in the new thread must use the worker-object approach; new slots should not be implemented directly into a subclassed :sip:ref:`~PyQt6.QtCore.QThread`.

Unlike queued slots or invoked methods, methods called directly on the :sip:ref:`~PyQt6.QtCore.QThread` object will execute in the thread that calls the method. When subclassing :sip:ref:`~PyQt6.QtCore.QThread`, keep in mind that the constructor executes in the old thread while :sip:ref:`~PyQt6.QtCore.QThread.run` executes in the new thread. If a member variable is accessed from both functions, then the variable is accessed from two different threads. Check that it is safe to do so.

**Note:** Care must be taken when interacting with objects across different threads. As a general rule, functions can only be called from the thread that created the :sip:ref:`~PyQt6.QtCore.QThread` object itself (e.g. :sip:ref:`~PyQt6.QtCore.QThread.setPriority`), unless the documentation says otherwise. See Synchronizing Threads for details.

.. _qthread-managing-threads:

Managing Threads
----------------

:sip:ref:`~PyQt6.QtCore.QThread` will notify you via a signal when the thread is :sip:ref:`~PyQt6.QtCore.QThread.started` and :sip:ref:`~PyQt6.QtCore.QThread.finished`, or you can use :sip:ref:`~PyQt6.QtCore.QThread.isFinished` and :sip:ref:`~PyQt6.QtCore.QThread.isRunning` to query the state of the thread.

You can stop the thread by calling :sip:ref:`~PyQt6.QtCore.QThread.exit` or :sip:ref:`~PyQt6.QtCore.QThread.quit`. In extreme cases, you may want to forcibly :sip:ref:`~PyQt6.QtCore.QThread.terminate` an executing thread. However, doing so is dangerous and discouraged. Please read the documentation for :sip:ref:`~PyQt6.QtCore.QThread.terminate` and :sip:ref:`~PyQt6.QtCore.QThread.setTerminationEnabled` for detailed information.

You often want to deallocate objects that live in a thread when a thread ends. To do this, connect the :sip:ref:`~PyQt6.QtCore.QThread.finished` signal to :sip:ref:`~PyQt6.QtCore.QObject.deleteLater`.

Use :sip:ref:`~PyQt6.QtCore.QThread.wait` to block the calling thread, until the other thread has finished execution (or until a specified time has passed).

:sip:ref:`~PyQt6.QtCore.QThread` also provides static, platform independent sleep functions: :sip:ref:`~PyQt6.QtCore.QThread.sleep`, :sip:ref:`~PyQt6.QtCore.QThread.msleep`, and :sip:ref:`~PyQt6.QtCore.QThread.usleep` allow full second, millisecond, and microsecond resolution respectively.

**Note:** :sip:ref:`~PyQt6.QtCore.QThread.wait` and the :sip:ref:`~PyQt6.QtCore.QThread.sleep` functions should be unnecessary in general, since Qt is an event-driven framework. Instead of :sip:ref:`~PyQt6.QtCore.QThread.wait`, consider listening for the :sip:ref:`~PyQt6.QtCore.QThread.finished` signal. Instead of the :sip:ref:`~PyQt6.QtCore.QThread.sleep` functions, consider using QChronoTimer.

The static functions :sip:ref:`~PyQt6.QtCore.QThread.currentThreadId` and :sip:ref:`~PyQt6.QtCore.QThread.currentThread` return identifiers for the currently executing thread. The former returns a platform specific ID for the thread; the latter returns a :sip:ref:`~PyQt6.QtCore.QThread` pointer.

To choose the name that your thread will be given (as identified by the command ``ps -L`` on Linux, for example), you can call :sip:ref:`~PyQt6.QtCore.QObject.setObjectName` before starting the thread. If you don't call :sip:ref:`~PyQt6.QtCore.QObject.setObjectName`, the name given to your thread will be the class name of the runtime type of your thread object (for example, ``"RenderThread"`` in the case of the `Mandelbrot <https://doc.qt.io/qt-6/qtcore-threads-mandelbrot-example.html>`_ example, as that is the name of the :sip:ref:`~PyQt6.QtCore.QThread` subclass). Note that this is currently not available with release builds on Windows.

.. seealso:: QThreadStorage, `Mandelbrot <https://doc.qt.io/qt-6/qtcore-threads-mandelbrot-example.html>`_, `Producer and Consumer using Semaphores <https://doc.qt.io/qt-6/qtcore-threads-semaphores-example.html>`_, `Producer and Consumer using Wait Conditions <https://doc.qt.io/qt-6/qtcore-threads-waitconditions-example.html>`_, Multi-threading in Qt.
