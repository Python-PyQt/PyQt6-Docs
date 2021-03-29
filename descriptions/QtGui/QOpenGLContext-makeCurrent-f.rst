.. sip:method-description::
    :status: todo
    :pysig: 9749538c1019986a5b9b693462930d4c
    :realsig: (QSurface*)
    :digest: 44329debd325345eacc4c2e9b6106dcc

Makes the context current in the current thread, against the given *surface*. Returns ``true`` if successful; otherwise returns ``false``. The latter may happen if the surface is not exposed, or the graphics hardware is not available due to e.g. the application being suspended.

If *surface* is ``nullptr`` this is equivalent to calling :sip:ref:`~PyQt6.QtGui.QOpenGLContext.doneCurrent`.

Avoid calling this function from a different thread than the one the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ instance lives in. If you wish to use `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ from a different thread you should first make sure it's not current in the current thread, by calling :sip:ref:`~PyQt6.QtGui.QOpenGLContext.doneCurrent` if necessary. Then call moveToThread(otherThread) before using it in the other thread.

By default Qt employs a check that enforces the above condition on the thread affinity. It is still possible to disable this check by setting the ``Qt::AA_DontCheckOpenGLContextThreadAffinity`` application attribute. Be sure to understand the consequences of using QObjects from outside the thread they live in, as explained in the QObject thread affinity documentation.

.. seealso:: functions(), :sip:ref:`~PyQt6.QtGui.QOpenGLContext.doneCurrent`, :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DontCheckOpenGLContextThreadAffinity`.
