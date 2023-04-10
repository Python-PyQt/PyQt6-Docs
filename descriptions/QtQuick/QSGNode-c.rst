.. sip:class-description::
    :status: todo
    :brief: The base class for all nodes in the scene graph
    :digest: 69d2b5e58000901008f72ab448c40336

The :sip:ref:`~PyQt6.QtQuick.QSGNode` class is the base class for all nodes in the scene graph.

The :sip:ref:`~PyQt6.QtQuick.QSGNode` class can be used as a child container. Children are added with the :sip:ref:`~PyQt6.QtQuick.QSGNode.appendChildNode`, :sip:ref:`~PyQt6.QtQuick.QSGNode.prependChildNode`, :sip:ref:`~PyQt6.QtQuick.QSGNode.insertChildNodeBefore` and :sip:ref:`~PyQt6.QtQuick.QSGNode.insertChildNodeAfter`. The order of nodes is important as geometry nodes are rendered according to their ordering in the scene graph.

The scene graph nodes contain a mechanism that describes which parts of the scene have changed. This includes the combined matrices, accumulated opacity, changes to the node hierarchy, and so on. This information can be used for optimizations inside the scene graph renderer. For the renderer to properly render the nodes, it is important that users call :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty` with the correct flags when nodes are changed. Most of the functions on the node classes will implicitly call :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty`. For example, :sip:ref:`~PyQt6.QtQuick.QSGNode.appendChildNode` will call :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty` passing in :sip:ref:`~PyQt6.QtQuick.QSGNode.DirtyState.DirtyNodeAdded`.

If nodes change every frame, the :sip:ref:`~PyQt6.QtQuick.QSGNode.preprocess` function can be used to apply changes to a node for every frame it is rendered. The use of :sip:ref:`~PyQt6.QtQuick.QSGNode.preprocess` must be explicitly enabled by setting the :sip:ref:`~PyQt6.QtQuick.QSGNode.Flag.UsePreprocess` flag on the node.

The virtual :sip:ref:`~PyQt6.QtQuick.QSGNode.isSubtreeBlocked` function can be used to disable a subtree all together. Nodes in a blocked subtree will not be preprocessed() and not rendered.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.
