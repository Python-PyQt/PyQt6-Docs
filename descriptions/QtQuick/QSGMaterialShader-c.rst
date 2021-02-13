.. sip:class-description::
    :status: todo
    :brief: Represents a graphics API independent shader program
    :digest: eb6e3241da02374db7937f4d9d57ff7d

The :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` class represents a graphics API independent shader program.

:sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` represents a combination of vertex and fragment shaders, data that define the graphics pipeline state changes, and logic that updates graphics resources, such as uniform buffers and textures.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

The :sip:ref:`~PyQt6.QtQuick.QSGMaterial` and :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` form a tight relationship. For one scene graph (including nested graphs), there is one unique :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` instance that encapsulates the shaders and other data the scene graph uses to render an object with that material. Each :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode` can have a unique :sip:ref:`~PyQt6.QtQuick.QSGMaterial` that defines how the graphics pipeline must be configured while drawing the node. An instance of :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` is never created explicitly by the user, it will be created on demand by the scene graph through :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader`. The scene graph creates an instance of :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` by calling the :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader` method, ensuring that there is only one instance of each shader implementation.

In Qt 5, :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` was tied to OpenGL. It was built directly on :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` and had functions like ``updateState()`` that could issue arbitrary OpenGL commands. This is no longer the case in Qt 6. :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` is not strictly data-oriented, meaning it provides data (shaders and the desired pipeline state changes) together with logic that updates data in a uniform buffer. Graphics API access is not provided. This means that a :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` cannot make OpenGL, Vulkan, Metal, or Direct 3D calls on its own. Together with the unified shader management, this allows a :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` to be written once, and be functional with any of the supported graphics APIs at run time.

The shaders set by calling the protected :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.setShaderFileName` function control what material does with the vertex data from the geometry, and how the fragments are shaded. A :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` will typically set a vertex and a fragment shader during construction. Changing the shaders afterwards may not lead to the desired effect and must be avoided.

In Qt 6, the default approach is to ship ``.qsb`` files with the application, typically embedded via the resource system, and referenced when calling :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.setShaderFileName`. The ``.qsb`` files are generated offline, or at latest at application build time, from Vulkan-style GLSL source code using the ``qsb`` tool from the Qt Shader Tools module.

There are three virtuals that can be overridden. These provide the data, or the logic to generate the data, for uniform buffers, textures, and pipeline state changes.

:sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateUniformData` is the function that is most commonly reimplemented in subclasses. This function is expected to update the contents of a :sip:ref:`~PyQt6.QtCore.QByteArray` that will then be exposed to the shaders as a uniform buffer. Any :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` that has a uniform block in its vertex or fragment shader must reimplement :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateUniformData`.

:sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateSampledImage` is relevant when the shader code samples textures. The function will be invoked for each sampler (or combined image sampler, in APIs where relevant), giving it the option to specify which :sip:ref:`~PyQt6.QtQuick.QSGTexture` should be exposed to the shader.

The shader pipeline state changes are less often used. One use case is materials that wish to use a specific blend mode. The relevant function is :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.updateGraphicsPipelineState`. This function is not called unless the :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` has opted in by setting the flag :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.Flags.UpdatesGraphicsPipelineState`. The task of the function is to update the :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.GraphicsPipelineState` struct instance that is passed to it with the desired changes. Currently only blending and culling-related features are available, other states cannot be controlled by materials.

A minimal example, that also includes texture support, could be the following. Here we assume that Material is the :sip:ref:`~PyQt6.QtQuick.QSGMaterial` that creates an instance of Shader in its :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader`, and that it holds a :sip:ref:`~PyQt6.QtQuick.QSGTexture` we want to sample in the fragment shader. The vertex shader relies only on the modelview-projection matrix.

::

    class Shader : public QSGMaterialShader
    {
    public:
        Shader()
        {
            setShaderFileName(VertexStage, QLatin1String(":/materialshader.vert.qsb"));
            setShaderFileName(FragmentStage, QLatin1String(":/materialshader.frag.qsb"));
        }

        bool updateUniformData(RenderState &state, QSGMaterial *, QSGMaterial *)
        {
            bool changed = false;
            QByteArray *buf = state.uniformData();
            if (state.isMatrixDirty()) {
                const QMatrix4x4 m = state.combinedMatrix();
                memcpy(buf->data(), m.constData(), 64);
                changed = true;
            }
            return changed;
        }

        void updateSampledImage(RenderState &, int binding, QSGTexture **texture, QSGMaterial *newMaterial, QSGMaterial *)
        {
            Material *mat = static_cast<Material *>(newMaterial);
            if (binding == 1)
                *texture = mat->texture();
        }
    };

The Vulkan-style GLSL source code for the shaders could look like the following. These are expected to be preprocessed offline using the ``qsb`` tool, which generates the ``.qsb`` files referenced in the Shader() constructor.

::

    #version 440
    layout(location = 0) in vec4 aVertex;
    layout(location = 1) in vec2 aTexCoord;
    layout(location = 0) out vec2 vTexCoord;
    layout(std140, binding = 0) uniform buf {
        mat4 qt_Matrix;
    } ubuf;
    out gl_PerVertex { vec4 gl_Position; };
    void main() {
        gl_Position = ubuf.qt_Matrix * aVertex;
        vTexCoord = aTexCoord;
    }

::

    #version 440
    layout(location = 0) in vec2 vTexCoord;
    layout(location = 0) out vec4 fragColor;
    layout(binding = 1) uniform sampler2D srcTex;
    void main() {
        vec4 c = texture(srcTex, vTexCoord);
        fragColor = vec4(c.rgb * 0.5, 1.0);
    }

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGMaterial`, `Scene Graph - Custom Material <https://doc.qt.io/qt-6/qtquick-scenegraph-custommaterial-example.html>`_, `Scene Graph - Two Texture Providers <https://doc.qt.io/qt-6/qtquick-scenegraph-twotextureproviders-example.html>`_, `Scene Graph - Graph <https://doc.qt.io/qt-6/qtquick-scenegraph-graph-example.html>`_.
