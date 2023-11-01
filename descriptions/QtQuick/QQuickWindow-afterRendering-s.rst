.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e7a687bdacc637b2aec2082e4548f7b3

The signal is emitted after scene graph has added its commands to the command buffer, which is not yet submitted to the graphics queue. If desired, the slot function connected to this signal can query native resources, like the command buffer, before via :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`. Note however that the render pass (or passes) are already recorded at this point and it is not possible to add more commands within the scenegraph's pass. Instead, use :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterRenderPassRecording` for that. This signal has therefore limited use in Qt 6, unlike in Qt 5. Rather, it is the combination of :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRenderPassRecording`, or :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterRenderPassRecording`, that is typically used to achieve under- or overlaying of the custom rendering.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

**Note:** When using OpenGL, be aware that setting OpenGL 3.x or 4.x specific states and leaving these enabled or set to non-default values when returning from the connected slot can interfere with the scene graph's rendering. The :sip:ref:`~PyQt6.QtGui.QOpenGLContext` used for rendering by the scene graph will be bound when the signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.rendererInterface`, `Scene Graph - RHI Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-rhiunderqml-example.html>`_, `Scene Graph - OpenGL Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-openglunderqml-example.html>`_, `Scene Graph - Metal Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-metalunderqml-example.html>`_, `Scene Graph - Vulkan Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-vulkanunderqml-example.html>`_, `Scene Graph - Direct3D 11 Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-d3d11underqml-example.html>`_.
