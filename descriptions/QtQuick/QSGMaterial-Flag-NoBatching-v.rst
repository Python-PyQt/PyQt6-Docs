.. sip:enum-member-description::
    :status: todo
    :value: 0x0010
    :digest: 94a9142934808d12a0874db2fd916ccc

Set this flag to true if the material uses shaders that are incompatible with the `scene graph's batching mechanism <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph-renderer.html>`_. This is relevant in certain advanced usages, such as, directly manipulating ``gl_Position.z`` in the vertex shader. Such solutions are often tied to a specific scene structure, and are likely not safe to use with arbitrary contents in a scene. Thus this flag should only be set after appropriate investigation, and will never be needed for the vast majority of materials. Setting this flag can lead to reduced performance due to having to issue more draw calls. This flag was introduced in Qt 6.3.
