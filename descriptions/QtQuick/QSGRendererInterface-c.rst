.. sip:class-description::
    :status: todo
    :brief: An interface providing access to some of the graphics API specific internals of the scenegraph
    :digest: 691a6a1a4bd511534e3c4947fe5cb6cc

An interface providing access to some of the graphics API specific internals of the scenegraph.

Renderer interfaces allow accessing graphics API specific functionality in the scenegraph. Such internals are not typically exposed. However, when integrating custom rendering via :sip:ref:`~PyQt6.QtQuick.QSGRenderNode` for example, it may become necessary to query certain values, for instance the graphics device (e.g. the Direct3D or Vulkan device) that is used by the scenegraph.

:sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`'s functions have varying availability. API and language queries, such as, :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.graphicsApi` or :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.shaderType` are always available, meaning it is sufficient to construct a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` or :sip:ref:`~PyQt6.QtQuick.QQuickView`, and the graphics API or shading language in use can be queried right after via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.rendererInterface`. This guarantees that utilities like the `GraphicsInfo <https://doc.qt.io/qt-6/qml-qtquick-graphicsinfo.html>`_ QML type are able to report the correct values as early as possible, without having conditional property values - depending on for instance :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.shaderType` - evaluate to unexpected values.

Engine-specific accessors, like :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.getResource`, are however available only after the scenegraph is initialized. Additionally, there may be backend-specific limitations on when such functions can be called. The only way that is guaranteed to succeed is calling them when the rendering of a node (i.e. the preparation of the command list for the next frame) is active. In practice this typically means :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.
