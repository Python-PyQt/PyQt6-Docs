.. sip:class-description::
    :status: todo
    :brief: Allows to use a textureId from a separate OpenGL context in a Qt 3D scene
    :realname: Qt3DRender::QSharedGLTexture
    :digest: 5277431db85d42394f7585e5f667d371

Allows to use a :sip:ref:`~PyQt6.Qt3DRender.QSharedGLTexture.textureId` from a separate OpenGL context in a Qt 3D scene.

Depending on the rendering mode used by Qt 3D, the shared context will either be:

* qt_gl_global_share_context when letting Qt 3D drive the rendering. When setting the attribute :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts` on the :sip:ref:`~PyQt6.QtWidgets.QApplication` class, this will automatically make :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` instances have their context shared with qt_gl_global_share_context.

* the shared context from the :sip:ref:`~PyQt6.QtQuick` scene. You might have to subclass :sip:ref:`~PyQt6.QtGui.QWindow` or use QtQuickRenderControl to have control over what that shared context is though as of 5.13 it is qt_gl_global_share_context.

Any 3rd party engine that shares its context with the Qt 3D renderer can now provide texture ids that will be referenced by the Qt 3D texture.

You can omit specifying the texture properties, Qt 3D will try at runtime to determine what they are. If you know them, you can of course provide them, avoid additional work for Qt 3D.

Keep in mind that if you are using custom materials and shaders, you need to specify the correct sampler type to be used.
