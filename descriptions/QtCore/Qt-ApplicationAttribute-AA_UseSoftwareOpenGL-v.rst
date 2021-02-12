.. sip:enum-member-description::
    :status: todo
    :value: 17
    :digest: 8851f65b65e47f9c32b3557a074b597a

Forces the usage of a software based OpenGL implementation on platforms that use dynamic loading of the OpenGL implementation. This will typically be a patched build of `Mesa llvmpipe <http://www.mesa3d.org/llvmpipe.html>`_, providing OpenGL 2.1. The value may have no effect if no such OpenGL implementation is available. The default name of this library is ``opengl32sw.dll`` and can be overridden by setting the environment variable *QT_OPENGL_DLL*. See the platform-specific pages, for instance Qt for Windows, for more information. This attribute must be set before QGuiApplication is constructed. This value was added in Qt 5.4.
