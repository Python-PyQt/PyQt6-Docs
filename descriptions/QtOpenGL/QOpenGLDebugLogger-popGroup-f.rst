.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e2d720b3cd0a365e4f35511ba3f9bd9d

Pops the topmost debug group from the debug groups stack. If the group is successfully popped, OpenGL will automatically log a message with message, id and source matching those of the popped group, type :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.GroupPopType` and severity :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.NotificationSeverity`.

Popping a debug group will restore the message filtering settings of the group that becomes the top of the debug groups stack.

**Note:** The object must be initialized before managing debug groups.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.pushGroup`.
