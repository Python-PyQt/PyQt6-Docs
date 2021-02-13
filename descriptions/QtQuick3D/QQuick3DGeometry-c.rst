.. sip:class-description::
    :status: todo
    :brief: Base class for defining custom geometry
    :digest: 6e6dc69c8c4d5101e410a6693c12dbb5

Base class for defining custom geometry.

The :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry` can be used to specify custom geometry for a Model in the Qt Quick 3D scene.

While not strictly required, the typical usage is to inherit from this class. The subclass is then exposed to QML by registering it to the type system. The `geometry <https://doc.qt.io/qt-6/qml-qtquick3d-model.html#geometry-prop>`_ property of a Model can then be set to reference an instance of the registered type.

The high-level structure of such a class is typically similar to the following:

::

    class CustomGeometry : public QQuick3DGeometry
    {
    public:
        CustomGeometry() { rebuildGeometry(); }

        void setSomething() {
           // Change relevant internal data.
           // ...

           // Then rebuild the vertex and index data and pass it to QQuick3DGeometry.
           rebuildGeometry();

           // Finally, trigger an update. This is relevant in case nothing else
           // is changing in the scene; this way we make sure a new frame will
           // be rendered.
           update();
        }

    private:
        void rebuildGeometry()
        {
            QByteArray vertices;
            QByteArray indices;
            ...
            setPrimitiveType(Lines);
            setVertexBuffer(vertices);
            setIndexBuffer(indices);
            setStride(3 * sizeof(float)); // e.g. when having 3 components per vertex
            setBounds(...); // minimum and maximum extents, for picking
            addAttribute(PositionSemantic, 0, F32Type);
            ...
        }
    };

This class can then be registered as a QML type and used with `Model <https://doc.qt.io/qt-6/qml-qtquick3d-model.html>`_.

In Qt 5 type registration happened with :sip:ref:`~PyQt6.QtQml.qmlRegisterType`:

::

    qmlRegisterType<CustomGeometry>("Example", 1, 0, "CustomGeometry");

In Qt 6 the default approach is to use automatic registration with the help of the build system. Instead of calling :sip:ref:`~PyQt6.QtQml.qmlRegisterType`, the ``.pro`` file can now contain:

::

    CONFIG += qmltypes
    QML_IMPORT_NAME = Example
    QML_IMPORT_MAJOR_VERSION = 1

Alternatively, with CMake the equivalent is:

::

    set_target_properties(application PROPERTIES
        QT_QML_MODULE_VERSION 1.0
        QT_QML_MODULE_URI Example
    )
    qt6_qml_type_registration(application)

The class implementation should add QML_NAMED_ELEMENT:

::

    class CustomGeometry : public QQuick3DGeometry
    {
        Q_OBJECT
        QML_NAMED_ELEMENT(CustomGeometry)
        ...
    };

The QML code can then use the custom type:

::

    import Example 1.0

    Model {
        id: customModel
        geometry: CustomGeometry {
        }
    }

At minimum, a custom geometry should have the following specified:

* vertex data,

* vertex stride,

* primitive type,

* an attribute with PositionSemantic.

These are sufficient to render the mesh. For indexed drawing, the index buffer data and an attribute with IndexSemantic needs to be specified as well. In order to support picking (input), the class must specify the bounding volume using :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.setBounds`. For proper lighting, an attribute with NormalSemantic is needed. When the material uses texturing, at least one set of UV coordinates must be provided and described in an TexCoordSemantic attribute. Some materials may require tangents and binormals as well.

As a concrete, minimal example, the following class would provide geometry for a single triangle:

::

    class ExampleGeometry : public QQuick3DGeometry
    {
        Q_OBJECT
        QML_NAMED_ELEMENT(ExampleGeometry)

    public:
        ExampleGeometry();

    private:
        void updateData();
    };

    ExampleGeometry::ExampleGeometry()
    {
        updateData();
    }

    void ExampleGeometry::updateData()
    {
        QByteArray v;
        v.resize(3 * 3 * sizeof(float));
        float *p = reinterpret_cast<float *>(v.data());

        // a triangle, front face = counter-clockwise
        *p++ = -1.0f; *p++ = -1.0f; *p++ = 0.0f;
        *p++ = 1.0f; *p++ = -1.0f; *p++ = 0.0f;
        *p++ = 0.0f; *p++ = 1.0f; *p++ = 0.0f;

        setVertexData(v);
        setStride(3 * sizeof(float));

        setPrimitiveType(QQuick3DGeometry::PrimitiveType::Triangles);

        addAttribute(QQuick3DGeometry::Attribute::PositionSemantic,
                     0,
                     QQuick3DGeometry::Attribute::F32Type);
    }

Depending on the lighting in the scene, the result of referencing this geometry from a Model:

.. image:: ../../../images/customgeometry.jpg

**Note:** Vertex data is expected to follow OpenGL conventions. This means the data must be provided with the assumption that the Y axis is pointing up in the normalized device coordinate system, and that front faces have a counter clockwise winding.

.. seealso:: `Model <https://doc.qt.io/qt-6/qml-qtquick3d-model.html>`_, `Geometry <https://doc.qt.io/qt-6/quick3d-asset-conditioning-3d-assets.html#geometry>`_.
