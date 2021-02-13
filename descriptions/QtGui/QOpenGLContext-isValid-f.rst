.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: b3695b9bdcee9d6ee4bb38970e24a790

Returns if this context is valid, i.e. has been successfully created.

On some platforms the return value of ``false`` for a context that was successfully created previously indicates that the OpenGL context was lost.

The typical way to handle context loss scenarios in applications is to check via this function whenever :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent` fails and returns ``false``. If this function then returns ``false``, recreate the underlying native OpenGL context by calling :sip:ref:`~PyQt6.QtGui.QOpenGLContext.create`, call :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent` again and then reinitialize all OpenGL resources.

On some platforms context loss situations is not something that can avoided. On others however, they may need to be opted-in to. This can be done by enabling :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.FormatOptions.ResetNotification` in the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`. This will lead to setting ``RESET_NOTIFICATION_STRATEGY_EXT`` to ``LOSE_CONTEXT_ON_RESET_EXT`` in the underlying native OpenGL context. `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ will then monitor the status via ``glGetGraphicsResetStatusEXT()`` in every :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOpenGLContext.create`.
