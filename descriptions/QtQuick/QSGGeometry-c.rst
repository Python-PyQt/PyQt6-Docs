.. sip:class-description::
    :status: todo
    :brief: Low-level storage for graphics primitives in the Qt Quick Scene Graph
    :digest: 16c415a1a18bf6fc5dab07fad017b50d

The :sip:ref:`~PyQt6.QtQuick.QSGGeometry` class provides low-level storage for graphics primitives in the `Qt Quick Scene Graph <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html>`_.

The :sip:ref:`~PyQt6.QtQuick.QSGGeometry` class stores the geometry of the primitives rendered with the scene graph. It contains vertex data and optionally index data. The mode used to draw the geometry, also called primitive topology, is specified with :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setDrawingMode`.

Vertices can be as simple as points defined by x and y values or can be more complex where each vertex contains a normal, texture coordinates and a 3D position. The :sip:ref:`~PyQt6.QtQuick.QSGGeometry.AttributeSet` is used to describe how the vertex data is built up. The attribute set can only be specified on construction. The :sip:ref:`~PyQt6.QtQuick.QSGGeometry` class provides a few convenience attributes and attribute sets by default. The :sip:ref:`~PyQt6.QtQuick.QSGGeometry.defaultAttributes_Point2D` function returns an attribute set to be used in normal solid color rectangles, while the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.defaultAttributes_TexturedPoint2D` function returns attributes to be used for textured 2D geometry. The vertex data is internally stored as a ``void \*`` and is accessible with the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.vertexData` function. Convenience accessors for the common attribute sets are available with :sip:ref:`~PyQt6.QtQuick.QSGGeometry.vertexDataAsPoint2D` and :sip:ref:`~PyQt6.QtQuick.QSGGeometry.vertexDataAsTexturedPoint2D`. Vertex data is allocated by passing a vertex count to the constructor or by calling :sip:ref:`~PyQt6.QtQuick.QSGGeometry.allocate` later.

The number of vertices and indices can be changed after construction by using the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.allocate` method to resize the data buffer. However, :sip:ref:`~PyQt6.QtQuick.QSGGeometry.allocate` requires updating all vertex and index data each time called. Since Qt 6.10, :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setVertexCount` and :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setIndexCount` allow adjusting the number of vertices or indices without reallocating the data buffer and only require updating new vertices or indices. In either case, the caller must mark the geometry node as dirty, by calling ``node->markDirty(QSGNode::DirtyGeometry)``, to ensure that the renderer has a chance to update internal buffers.

The :sip:ref:`~PyQt6.QtQuick.QSGGeometry` can optionally contain indices of either unsigned 32-bit, unsigned 16-bit, or unsigned 8-bit integers. The index type must be specified during construction and cannot be changed.

Below is a snippet illustrating how a geometry composed of position and color vertices can be built.

::

    struct MyPoint2D {
        float x;
        float y;
        float r;
        float g;
        float b;
        float a;

        void set(float x_, float y_, float r_, float g_, float b_, float a_) {
            x = x_;
            y = y_;
            r = r_;
            g = g_;
            b = b_;
            a = a_;
        }
    };

    QSGGeometry::Attribute MyPoint2D_Attributes[] = {
        QSGGeometry::Attribute::create(0, 2, FloatType, true),
        QSGGeometry::Attribute::create(1, 4, FloatType, false)
    };

    QSGGeometry::AttributeSet MyPoint2D_AttributeSet = {
        2,
        sizeof(MyPoint2D),
        MyPoint2D_Attributes
    };

    ...

    geometry = new QSGGeometry(MyPoint2D_AttributeSet, 2);
    geometry->setDrawingMode(DrawLines);

    MyPoint2D *vertices = static_cast<MyPoint2D *>(geometry->vertexData());
    vertices[0].set(0, 0, 1, 0, 0, 1);
    vertices[1].set(width(), height(), 0, 0, 1, 1);

The :sip:ref:`~PyQt6.QtQuick.QSGGeometry` is a software buffer and client-side in terms of accelerated rendering, as the buffers used in 2D graphics typically consist of many small buffers that change every frame and do not benefit from being uploaded to graphics memory. However, the :sip:ref:`~PyQt6.QtQuick.QSGGeometry` supports hinting to the renderer that a buffer should be uploaded using the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setVertexDataPattern` and :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setIndexDataPattern` functions. Whether this hint is respected or not is implementation specific.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode`, `Scene Graph - Custom Geometry <https://doc.qt.io/qt-6/qtquick-scenegraph-customgeometry-example.html>`_.
