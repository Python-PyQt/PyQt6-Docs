.. sip:class-description::
    :status: todo
    :brief: Base class for defining custom texture data
    :digest: be39008a502d247cf596a93e01779e1f

Base class for defining custom texture data.

The :sip:ref:`~PyQt6.QtQuick3D.QQuick3DTextureData` class can be used to specify custom texture data for a `Texture <https://doc.qt.io/qt-6/qml-qtquick3d-texture.html>`_ in a Qt Quick 3D scene.

While not strictly required, the typical usage is to inherit from this class. The subclass is then exposed to QML by registering it to the type system. The `textureData <https://doc.qt.io/qt-6/qml-qtquick3d-texture.html#textureData-prop>`_ property of a `Texture <https://doc.qt.io/qt-6/qml-qtquick3d-texture.html>`_ can then be set to reference an instance of the registered type.

Example implementation:

::

    class CustomTextureData : public QQuick3DTextureData
    {
        Q_OBJECT
        ... properties ...

    public:
        CustomTextureData() { regenerateTextureData(); }

        void setProperty(...)
        {
            // Change relevant internal data.
            // ...

            // Update the texture data
            regenerateTextureData();

            // Finally, trigger an update. This is relevant in case nothing else
            // is changed in the scene; this way we make sure a new frame will
            // be rendered
            update();
        }
    private:
        void regenerateTextureData()
        {
            QByteArray textureData;
            textureData = generateTextureData();
            setTextureData(textureData);
            setSize(QSize(256, 256));
            setFormat(QQuick3DTextureData::Format::RGBA8)
            setHasTransparency(true);
        }
    };

This class can then be registered as a QML type and used with `Texture <https://doc.qt.io/qt-6/qml-qtquick3d-texture.html>`_.

In Qt 5 type registration happened with :sip:ref:`~PyQt6.QtQml.qmlRegisterType`:

::

    qmlRegisterType<MyCustomTextureData>("Example", 1, 0, "MyCustomTextureData");

In Qt 6 the default approach is to use automatic registration with the help of the build system. Instead of calling :sip:ref:`~PyQt6.QtQml.qmlRegisterType`, the ``.pro`` file can now contain:

::

    CONFIG += qmltypes
    QML_IMPORT_NAME = Example
    QML_IMPORT_MAJOR_VERSION = 1

With CMake, automatic registration is the default behavior, so no special settings are needed beyond basic QML module setup:

::

    qt_add_qml_module(application
        URI Example
        VERSION 1.0
    )

The class implementation should add QML_NAMED_ELEMENT:

::

    class CustomTextureData : public QQuick3DTextureData
    {
        Q_OBJECT
        QML_NAMED_ELEMENT(MyCustomTextureData)
        ...
    };

The QML code can then use the custom type:

::

    import Example 1.0

    Model {
        source: "#Cube"
        materials: [
            DefaultMaterial {
                diffuseMap: diffuseMapCustomTexture
            }
        ]
        Texture {
            id: diffuseMapCustomTexture
            textureData: MyCustomTextureData { }
        }
    }
