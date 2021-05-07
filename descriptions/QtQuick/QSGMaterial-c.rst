.. sip:class-description::
    :status: todo
    :brief: Encapsulates rendering state for a shader program
    :digest: 43b847acec9f8f5654b5bd72f3cc5443

The :sip:ref:`~PyQt6.QtQuick.QSGMaterial` class encapsulates rendering state for a shader program.

:sip:ref:`~PyQt6.QtQuick.QSGMaterial` and :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` subclasses form a tight relationship. For one scene graph (including nested graphs), there is one unique :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` instance which encapsulates the shaders the scene graph uses to render that material, such as a shader to flat coloring of geometry. Each :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode` can have a unique :sip:ref:`~PyQt6.QtQuick.QSGMaterial` containing the how the shader should be configured when drawing that node, such as the actual color to used to render the geometry.

:sip:ref:`~PyQt6.QtQuick.QSGMaterial` has two virtual functions that both need to be implemented. The function :sip:ref:`~PyQt6.QtQuick.QSGMaterial.type` should return a unique instance for all instances of a specific subclass. The :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader` function should return a new instance of :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader`, specific to that subclass of :sip:ref:`~PyQt6.QtQuick.QSGMaterial`.

A minimal :sip:ref:`~PyQt6.QtQuick.QSGMaterial` implementation could look like this:

::

    class Material : public QSGMaterial
    {
    public:
        QSGMaterialType *type() const override { static QSGMaterialType type; return &type; }
        QSGMaterialShader *createShader(QSGRendererInterface::RenderMode) const override { return new Shader; }
    };

See the `Custom Material example <https://doc.qt.io/qt-6/qtquick-scenegraph-custommaterial-example.html>`_ for an introduction on implementing a :sip:ref:`~PyQt6.QtQuick.QQuickItem` subclass backed by a :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode` and a custom material.

**Note:** :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader` is called only once per :sip:ref:`~PyQt6.QtQuick.QSGMaterialType`, to reduce redundant work with shader preparation. If a :sip:ref:`~PyQt6.QtQuick.QSGMaterial` is backed by multiple sets of vertex and fragment shader combinations, the implementation of :sip:ref:`~PyQt6.QtQuick.QSGMaterial.type` must return a different, unique :sip:ref:`~PyQt6.QtQuick.QSGMaterialType` pointer for each combination of shaders.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader`, `Scene Graph - Custom Material <https://doc.qt.io/qt-6/qtquick-scenegraph-custommaterial-example.html>`_, `Scene Graph - Two Texture Providers <https://doc.qt.io/qt-6/qtquick-scenegraph-twotextureproviders-example.html>`_, `Scene Graph - Graph <https://doc.qt.io/qt-6/qtquick-scenegraph-graph-example.html>`_.
