.. sip:class-description::
    :status: todo
    :brief: Mechanism for rendering the Qt Quick scenegraph onto an offscreen render target in a fully application-controlled manner
    :digest: f72c83914cdfca405f1ac79e843dc72c

The :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` class provides a mechanism for rendering the Qt Quick scenegraph onto an offscreen render target in a fully application-controlled manner.

:sip:ref:`~PyQt6.QtQuick.QQuickWindow` and :sip:ref:`~PyQt6.QtQuick.QQuickView` and their associated internal render loops render the Qt Quick scene onto a native window. In some cases, for example when integrating with 3rd party OpenGL, Vulkan, Metal, or Direct 3D renderers, it can be useful to get the scene into a texture that can then be used in arbitrary ways by the external rendering engine. Such a mechanism is also essential when integrating with a VR framework. :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` makes this possible in a hardware accelerated manner, unlike the performance-wise limited alternative of using :sip:ref:`~PyQt6.QtQuick.QQuickWindow.grabWindow`

When using a :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` does not have to be shown or even created at all. This means there will not be an underlying native window for it. Instead, the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instance is associated with the render control, using the overload of the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` constructor, and a texture or image object specified via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`.

Management of the graphics devices, contexts, image and texture objects is up to the application. The device or context that will be used by Qt Quick must be created before calling :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`. The creation of the the texture object can be deferred, see below. Qt 5.4 introduces the ability for `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ to adopt existing native contexts. Together with :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` this makes it possible to create a `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ that shares with an external rendering engine's existing context. This new `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ can then be used to render the Qt Quick scene into a texture that is accessible by the other engine's context too. For Vulkan, Metal, and Direct 3D there are no Qt-provided wrappers for device objects, so existing ones can be passed as-is via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice`.

Loading and instantiation of the QML components happen by using a :sip:ref:`~PyQt6.QtQml.QQmlEngine`. Once the root object is created, it will need to be parented to the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`'s contentItem().

Applications will usually have to connect to 4 important signals:

* :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized` Emitted at some point after calling :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`. Upon this signal, the application is expected to create its framebuffer object and associate it with the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

* :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated` When the scenegraph resources are released, the framebuffer object can be destroyed too.

* :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.renderRequested` Indicates that the scene has to be rendered by calling :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.render`. After making the context current, applications are expected to call :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.render`.

* :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sceneChanged` Indicates that the scene has changed meaning that, before rendering, polishing and synchronizing is also necessary.

To send events, for example mouse or keyboard events, to the scene, use :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendEvent` with the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instance as the receiver.

**Note:** In general :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` is supported in combination with all Qt Quick backends. However, some functionality, in particular grab(), may not be available in all cases.
