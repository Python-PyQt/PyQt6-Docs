.. sip:class-description::
    :status: todo
    :brief: Provided for convenience to easily draw textured content using the QML scene graph
    :digest: 89421de5f0a985f30c9345a39c9fee72

The :sip:ref:`~PyQt6.QtQuick.QSGSimpleTextureNode` class is provided for convenience to easily draw textured content using the QML scene graph.

**Warning:** The simple texture node class must have a texture before being added to the scene graph to be rendered.

**Warning:** This utility class is only functional when running with the default or software backends of the Qt Quick scenegraph. As an alternative, prefer using :sip:ref:`~PyQt6.QtQuick.QSGImageNode` via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.createImageNode`. However, this standalone class is still useful when used via subclassing and the application knows that no special scenegraph backends will be involved.
