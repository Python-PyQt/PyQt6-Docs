.. sip:class-description::
    :status: todo
    :brief: Implements transformations in the scene graph
    :digest: 5f051b93494cc1a5944e1d2a5d210da4

The :sip:ref:`~PyQt6.QtQuick.QSGTransformNode` class implements transformations in the scene graph.

Transformations apply the node's subtree and can be nested. Multiple transform nodes will be accumulated by intersecting all their matrices. The accumulation happens as part of the rendering.

The transform nodes implement a 4x4 matrix which in theory supports full 3D transformations. However, because the renderer optimizes for 2D use-cases rather than 3D use-cases, rendering a scene with full 3D transformations needs to be done with some care.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.
