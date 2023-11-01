.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6ad91d359499a1882476187985ee0817

This signal is emitted after the preparations for the frame have been done, meaning there is a command buffer in recording mode, where applicable. If desired, the slot function connected to this signal can query native resources like the command before via :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`. Note however that the recording of the main render pass is not yet started at this point and it is not possible to add commands within that pass. Starting a pass means clearing the color, depth, and stencil buffers so it is not possible to achieve an underlay type of rendering by just connecting to this signal. Rather, connect to :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRenderPassRecording`. However, connecting to this signal is still important if the recording of copy type of commands is desired since those cannot be enqueued within a render pass.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

**Note:** When using OpenGL, be aware that setting OpenGL 3.x or 4.x specific states and leaving these enabled or set to non-default values when returning from the connected slot can interfere with the scene graph's rendering. The :sip:ref:`~PyQt6.QtGui.QOpenGLContext` used for rendering by the scene graph will be bound when the signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.rendererInterface`, `Scene Graph - RHI Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-rhiunderqml-example.html>`_, `Scene Graph - OpenGL Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-openglunderqml-example.html>`_, `Scene Graph - Metal Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-metalunderqml-example.html>`_, `Scene Graph - Vulkan Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-vulkanunderqml-example.html>`_, `Scene Graph - Direct3D 11 Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-d3d11underqml-example.html>`_.
