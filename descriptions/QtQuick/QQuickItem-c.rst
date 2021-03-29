.. sip:class-description::
    :status: todo
    :brief: The most basic of all visual items in Qt Quick
    :digest: 681433e6a2c69b5357f2ecb4b4cd0f09

The :sip:ref:`~PyQt6.QtQuick.QQuickItem` class provides the most basic of all visual items in `Qt Quick <https://doc.qt.io/qt-6/qtquick-index.html>`_.

All visual items in Qt Quick inherit from :sip:ref:`~PyQt6.QtQuick.QQuickItem`. Although a :sip:ref:`~PyQt6.QtQuick.QQuickItem` instance has no visual appearance, it defines all the attributes that are common across visual items, such as x and y position, width and height, `anchoring <https://doc.qt.io/qt-6/qtquick-positioning-anchors.html>`_ and key handling support.

You can subclass :sip:ref:`~PyQt6.QtQuick.QQuickItem` to provide your own custom visual item that inherits these features.

.. _qquickitem-custom-scene-graph-items:

Custom Scene Graph Items
------------------------

All visual QML items are rendered using the scene graph, the default implementation of which is a low-level, high-performance rendering stack, closely tied to accelerated graphics APIs, such as OpenGL, Vulkan, Metal, or Direct 3D. It is possible for subclasses of :sip:ref:`~PyQt6.QtQuick.QQuickItem` to add their own custom content into the scene graph by setting the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flags.ItemHasContents` flag and reimplementing the :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode` function.

**Warning:** It is crucial that graphics operations and interaction with the scene graph happens exclusively on the rendering thread, primarily during the :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode` call. The best rule of thumb is to only use classes with the "QSG" prefix inside the :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode` function.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

.. _qquickitem-graphics-resource-handling:

Graphics Resource Handling
..........................

The preferred way to handle cleanup of graphics resources used in the scene graph, is to rely on the automatic cleanup of nodes. A :sip:ref:`~PyQt6.QtQuick.QSGNode` returned from :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode` is automatically deleted on the right thread at the right time. Trees of :sip:ref:`~PyQt6.QtQuick.QSGNode` instances are managed through the use of :sip:ref:`~PyQt6.QtQuick.QSGNode.Flags.OwnedByParent`, which is set by default. So, for the majority of custom scene graph items, no extra work will be required.

Implementations that store graphics resources outside the node tree, such as an item implementing :sip:ref:`~PyQt6.QtQuick.QQuickItem.textureProvider`, will need to take care in cleaning it up correctly depending on how the item is used in QML. The situations to handle are:

* The scene graph is invalidated; This can happen, depending on the platform and :sip:ref:`~PyQt6.QtQuick.QQuickWindow` configuration, when the window is hidden using QQuickWindow::hide(), or when it is closed. If the item class implements a ``slot`` named ``invalidateSceneGraph()``, this slot will be called on the rendering thread while the GUI thread is blocked. This is equivalent to connecting to :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated`. When rendering through OpenGL, the OpenGL context of this item's window will be bound when this slot is called. The only exception is if the native OpenGL has been destroyed outside Qt's control, for instance through ``EGL_CONTEXT_LOST``.

* The item is removed from the scene; If an item is taken out of the scene, for instance because it's parent was set to ``null`` or an item in another window, the :sip:ref:`~PyQt6.QtQuick.QQuickItem.releaseResources` will be called on the GUI thread. :sip:ref:`~PyQt6.QtQuick.QQuickWindow.scheduleRenderJob` should be used to schedule cleanup of rendering resources.

* The item is deleted; When the destructor if an item runs, it should delete any graphics resources it has. If neither of the two conditions above were already met, the item will be part of a window and it is possible to use :sip:ref:`~PyQt6.QtQuick.QQuickWindow.scheduleRenderJob` to have them cleaned up. If an implementation ignores the call to :sip:ref:`~PyQt6.QtQuick.QQuickItem.releaseResources`, the item will in many cases no longer have access to a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` and thus no means of scheduling cleanup.

When scheduling cleanup of graphics resources using :sip:ref:`~PyQt6.QtQuick.QQuickWindow.scheduleRenderJob`, one should use either :sip:ref:`~PyQt6.QtQuick.QQuickWindow.RenderStage.BeforeSynchronizingStage` or :sip:ref:`~PyQt6.QtQuick.QQuickWindow.RenderStage.AfterSynchronizingStage`. The `synchronization stage <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ is where the scene graph is changed as a result of changes to the QML tree. If cleanup is scheduled at any other time, it may result in other parts of the scene graph referencing the newly deleted objects as these parts have not been updated.

**Note:** Use of :sip:ref:`~PyQt6.QtCore.QObject.deleteLater` to clean up graphics resources is strongly discouraged as this will make the ``delete`` operation run at an arbitrary time and it is unknown if there will be an OpenGL context bound when the deletion takes place.

.. _qquickitem-custom-qpainter-items:

Custom QPainter Items
---------------------

The :sip:ref:`~PyQt6.QtQuick.QQuickItem` provides a subclass, :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem`, which allows the users to render content using :sip:ref:`~PyQt6.QtGui.QPainter`.

**Warning:** Using :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem` uses an indirect 2D surface to render its content, using software rasterization, so the rendering is a two-step operation. First rasterize the surface, then draw the surface. Using scene graph API directly is always significantly faster.

.. _qquickitem-behavior-animations:

Behavior Animations
-------------------

If your Item uses the `Behavior <https://doc.qt.io/qt-6/qml-qtquick-behavior.html>`_ type to define animations for property changes, you should always use either :sip:ref:`~PyQt6.QtCore.QObject.setProperty`, QQmlProperty(), or :sip:ref:`~PyQt6.QtCore.QMetaProperty.write` when you need to modify those properties from C++. This ensures that the QML engine knows about the property change. Otherwise, the engine won't be able to carry out your requested animation. Note that these functions incur a slight performance penalty. For more details, see `Accessing Members of a QML Object Type from C++ <https://doc.qt.io/qt-6/qtqml-cppintegration-interactqmlfromcpp.html#accessing-members-of-a-qml-object-type-from-c>`_.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem`.
