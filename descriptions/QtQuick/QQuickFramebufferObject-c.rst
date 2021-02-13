.. sip:class-description::
    :status: todo
    :brief: Convenience class for integrating OpenGL rendering using a framebuffer object (FBO) with Qt Quick
    :digest: 8b4fde5a21fb8b9ddd16cdc9c519ac14

The :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject` class is a convenience class for integrating OpenGL rendering using a framebuffer object (FBO) with Qt Quick.

**Warning:** This class is only functional when Qt Quick is rendering via OpenGL. It is not compatible with other graphics APIs, such as Vulkan or Metal. It should be treated as a legacy class that is only present in order to enable Qt 5 applications to function without source compatibility breaks as long as they tie themselves to OpenGL.

On most platforms, the rendering will occur on a `dedicated thread <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_. For this reason, the :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject` class enforces a strict separation between the item implementation and the FBO rendering. All item logic, such as properties and UI-related helper functions needed by QML should be located in a :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject` class subclass. Everything that relates to rendering must be located in the :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.Renderer` class.

To avoid race conditions and read/write issues from two threads it is important that the renderer and the item never read or write shared variables. Communication between the item and the renderer should primarily happen via the :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.Renderer.synchronize` function. This function will be called on the render thread while the GUI thread is blocked.

Using queued connections or events for communication between item and renderer is also possible.

Both the Renderer and the FBO are memory managed internally.

To render into the FBO, the user should subclass the Renderer class and reimplement its :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.Renderer.render` function. The Renderer subclass is returned from :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.createRenderer`.

The size of the FBO will by default adapt to the size of the item. If a fixed size is preferred, set :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.textureFollowsItemSize` to ``false`` and return a texture of your choosing from :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.Renderer.createFramebufferObject`.

Starting Qt 5.4, the :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject` class is a :sip:ref:`~PyQt6.QtQuick.QSGTextureProvider` and can be used directly in `ShaderEffects <https://doc.qt.io/qt-6/qml-qtquick-shadereffect.html>`_ and other classes that consume texture providers.

.. seealso:: `Scene Graph - Rendering FBOs <https://doc.qt.io/qt-6/qtquick-scenegraph-fboitem-example.html>`_, `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_.
