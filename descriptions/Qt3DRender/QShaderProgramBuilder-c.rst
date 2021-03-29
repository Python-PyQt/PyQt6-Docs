.. sip:class-description::
    :status: todo
    :brief: Generates a Shader Program content from loaded graphs
    :realname: Qt3DRender::QShaderProgramBuilder
    :digest: a67f034787d6260d8c048489295b2514

Generates a Shader Program content from loaded graphs.

A shader program builder consists of several different shader graphs used to generate shader code.

A cache of generated shader code is maintained. Generated shaders are by defaults saved in :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`\ (\ :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.TempLocation`)). This path can be overridden by setting environment variable QT3D_WRITABLE_CACHE_PATH to a valid writable path.

The use of the cache can be disabled by setting environment variable QT3D_DISABLE_SHADER_CACHE.

In most cases, changes made to a graph are detected by Qt 3D and a new cache entry will be generated. One case were this will not happen is when code snippets included by a graphs are changed. To work around that, clearing the cache directory or setting environment variable QT3D_REBUILD_SHADER_CACHE can be used to force shader code to be generated again.
