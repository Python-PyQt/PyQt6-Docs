.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 6841aab016f6c89c3ab2b2340d5ebc56

Returns The number of views in case of the material is used in multiview rendering.

**Note:** The return value is valid only when called from :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader`, and afterwards. The value is not necessarily up-to-date before :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader` is invokved by the scene graph.

Normally the return value is ``1``. A view count greater than 2 implies a *multiview render pass*. Materials that support multiview are expected to query viewCount() in :sip:ref:`~PyQt6.QtQuick.QSGMaterial.createShader`, or in their :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` constructor, and ensure the appropriate shaders are picked. The vertex shader is then expected to use ``gl_ViewIndex`` to index the modelview-projection matrix array as there are multiple matrices in multiview mode. (one for each view)

As an example, take the following simple vertex shader:

::

    #version 440

    layout(location = 0) in vec4 vertexCoord;
    layout(location = 1) in vec4 vertexColor;

    layout(location = 0) out vec4 color;

    layout(std140, binding = 0) uniform buf {
        mat4 matrix[2];
        float opacity;
    };

    void main()
    {
        gl_Position = matrix[gl_ViewIndex] * vertexCoord;
        color = vertexColor * opacity;
    }

This shader is prepared to handle 2 views, and 2 views only. It is not compatible with other view counts. When conditioning the shader, the ``qsb`` tool has to be invoked with ``--view-count 2`` or, if using the CMake integration, ``VIEW_COUNT 2`` must be specified in the ``qt_add_shaders()`` command.

**Note:** A line with ``#extension GL_EXT_multiview : require`` is injected automatically by ``qsb`` whenever a view count of 2 or greater is set.

Developers are encouraged to use the automatically injected preprocessor variable ``QSHADER_VIEW_COUNT`` to simplify the handling of the different number of views. For example, if there is a need to support both non-multiview and multiview with a view count of 2 in the same source file, the following could be done:

::

    #version 440

    layout(location = 0) in vec4 vertexCoord;
    layout(location = 1) in vec4 vertexColor;

    layout(location = 0) out vec4 color;

    layout(std140, binding = 0) uniform buf {
    #if QSHADER_VIEW_COUNT >= 2
        mat4 matrix[QSHADER_VIEW_COUNT];
    #else
        mat4 matrix;
    #endif
        float opacity;
    };

    void main()
    {
    #if QSHADER_VIEW_COUNT >= 2
        gl_Position = matrix[gl_ViewIndex] * vertexCoord;
    #else
        gl_Position = matrix * vertexCoord;
    #endif
        color = vertexColor * opacity;
    }

The same source file can now be run through ``qsb`` or ``qt_add_shaders()`` twice, once without specify the view count, and once with the view count set to 2. The material can then pick the appropriate .qsb file based on viewCount() at run time.

With CMake, this could looks similar to the following. With this example the corresponding :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader` is expected to choose between ``:/shaders/example.vert.qsb`` and ``:/shaders/multiview/example.vert.qsb`` based on the value of viewCount(). (same goes for the fragment shader)

::

    qt_add_shaders(application "application_shaders"
        PREFIX
            /
        FILES
            shaders/example.vert
            shaders/example.frag
    )

    qt_add_shaders(application "application_multiview_shaders"
        GLSL
            330,300es
        HLSL
            61
        MSL
            12
        VIEW_COUNT
            2
        PREFIX
            /
        FILES
            shaders/example.vert
            shaders/example.frag
        OUTPUTS
            shaders/multiview/example.vert
            shaders/multiview/example.frag
    )

**Note:** The fragment shader should be treated the same way the vertex shader is, even though the fragment shader code cannot have any dependency on the view count (``gl_ViewIndex``), for maximum portability. There are two reasons for including fragment shaders too in the multiview set. One is that mixing different shader versions within the same graphics pipeline can be problematic, depending on the underlying graphics API: with D3D12 for example, mixing HLSL shaders for shader model 5.0 and 6.1 would generate an error. The other is that having ``QSHADER_VIEW_COUNT`` defined in fragment shaders can be very useful, for example when sharing a uniform buffer layout between the vertex and fragment stages.

**Note:** For OpenGL the minimum GLSL version for vertex shaders relying on ``gl_ViewIndex`` is ``330``. Lower versions may be accepted at build time, but may lead to an error at run time, depending on the OpenGL implementation.

As a convenience, there is also a ``MULTIVIEW`` option for qt_add_shaders(). This first runs the ``qsb`` tool normally, then overrides ``VIEW_COUNT`` to ``2``, sets ``GLSL``, ``HLSL``, ``MSL`` to some suitable defaults, and runs ``qsb`` again, this time outputting .qsb files with a suffix added. The material implementation can then use the :sip:ref:`~PyQt6.QtQuick.QSGMaterialShader.setShaderFileName` overload taking a ``viewCount`` argument, that automatically picks the correct .qsb file.

The following is therefore mostly equivalent to the example call shown above, except that no manually managed output files need to be specified. Note that there can be cases when the automatically chosen shading language versions are not sufficient, in which case applications should continue specify everything explicitly.

::

    qt_add_shaders(application "application_multiview_shaders"
        MULTIVIEW
        PREFIX
            /
        FILES
            shaders/example.vert
            shaders/example.frag
    )

See QRhi::MultiView, QRhiColorAttachment::setMultiViewCount(), and QRhiGraphicsPipeline::setMultiViewCount() for further, lower-level details on multiview support in Qt. The Qt Quick scene graph renderer is prepared to recognize multiview render targets, when specified via QQuickRenderTarget::fromRhiRenderTarget() or the 3D API specific functions, such as fromVulkanImage() with an ``arraySize`` argument greater than 1. The renderer will then propagate the view count to graphics pipelines and the materials.
