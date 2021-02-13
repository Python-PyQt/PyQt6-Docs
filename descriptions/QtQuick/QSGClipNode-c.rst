.. sip:class-description::
    :status: todo
    :brief: Implements the clipping functionality in the scene graph
    :digest: a51bfc60c74f329f6f9cb51aaa182836

The :sip:ref:`~PyQt6.QtQuick.QSGClipNode` class implements the clipping functionality in the scene graph.

Clipping applies to the node's subtree and can be nested. Multiple clip nodes will be accumulated by intersecting all their geometries. The accumulation happens as part of the rendering.

Clip nodes must have a geometry before they can be added to the scene graph.

Clipping is usually implemented by using the stencil buffer.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.
