.. sip:class-description::
    :status: todo
    :brief: Used for all rendered content in the scene graph
    :digest: 5f94afe799d97f80027b3fcfbc0cef3d

The :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode` class is used for all rendered content in the scene graph.

The :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode` consists of geometry and material. The geometry defines the mesh, the vertices and their structure, to be drawn. The Material defines how the shape is filled.

The following is a code snippet illustrating how to create a red line using a :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode`:

::

    QSGGeometry *geometry = new QSGGeometry(QSGGeometry::defaultAttributes_Point2D(), 2);
    geometry->setDrawingMode(GL_LINES);
    geometry->setLineWidth(3);
    geometry->vertexDataAsPoint2D()[0].set(0, 0);
    geometry->vertexDataAsPoint2D()[1].set(width(), height());

    QSGFlatColorMaterial *material = new QSGFlatColorMaterial;
    material->setColor(QColor(255, 0, 0));

    QSGGeometryNode *node = new QSGGeometryNode;
    node->setGeometry(geometry);
    node->setFlag(QSGNode::OwnsGeometry);
    node->setMaterial(material);
    node->setFlag(QSGNode::OwnsMaterial);

A geometry node must have both geometry and a normal material before it is added to the scene graph. When the geometry and materials are changed after the node has been added to the scene graph, the user should also mark them as dirty using :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty`.

The geometry node supports two types of materials, the :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode.opaqueMaterial` and the normal material. The :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode.opaqueMaterial` is used when the accumulated scene graph opacity at the time of rendering is 1. The primary use case is to special case opaque rendering to avoid an extra operation in the fragment shader can have significant performance impact on embedded graphics chips. The opaque material is optional.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry`, :sip:ref:`~PyQt6.QtQuick.QSGMaterial`.
