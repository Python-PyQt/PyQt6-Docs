.. sip:method-description::
    :status: todo
    :pysig: 95d6ecc23a91ff19cbd3971ba88a282b
    :realsig: (const QString&,GLuint,QOpenGLDebugMessage::Source)
    :digest: 6c06f408e45d74dd19f6a7e551bec265

Pushes a debug group with name *name*, id *id*, and source *source* onto the debug groups stack. If the group is successfully pushed, OpenGL will automatically log a message with message *name*, id *id*, source *source*, type :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.GroupPushType` and severity :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.NotificationSeverity`.

The newly pushed group will inherit the same filtering settings of the group that was on the top of the stack; that is, the filtering will not be changed by pushing a new group.

**Note:** The *source* must either be :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.ApplicationSource` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.ThirdPartySource`, otherwise the group will not be pushed.

**Note:** The object must be initialized before managing debug groups.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.popGroup`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.enableMessages`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.disableMessages`.
