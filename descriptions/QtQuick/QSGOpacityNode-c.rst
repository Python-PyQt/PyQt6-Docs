.. sip:class-description::
    :status: todo
    :brief: Used to change opacity of nodes
    :digest: 531f8a345757a1029af55bb37baf0ef7

The :sip:ref:`~PyQt6.QtQuick.QSGOpacityNode` class is used to change opacity of nodes.

Opacity applies to its subtree and can be nested. Multiple opacity nodes will be accumulated by multiplying their opacity. The accumulation happens as part of the rendering.

When nested opacity gets below a certain threshold, the subtree might be marked as blocked, causing isSubtreeBlocked() to return true. This is done for performance reasons.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.
