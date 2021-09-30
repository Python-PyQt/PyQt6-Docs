.. sip:method-description::
    :status: todo
    :pysig: 2897ad28422feb81fb69591826b72180
    :realsig: (uint,const QSize&,int)
    :digest: 2e949160d7262f1f0702afefe44876db

Returns a new :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` referencing an OpenGL renderbuffer object specified by *renderbufferId*.

The renderbuffer will be used as the color attachment for the internal framebuffer object. This function is provided to allow targeting renderbuffers that are created by the application with some external buffer underneath, such as an EGLImageKHR. Once the application has called `glEGLImageTargetRenderbufferStorageOES <https://www.khronos.org/registry/OpenGL/extensions/OES/OES_EGL_image.txt>`_, the renderbuffer can be passed to this function.

*pixelSize* specifies the size of the image, in pixels.

*sampleCount* specific the number of samples. 0 or 1 means no multisampling, while a value like 4 or 8 states that the native object is a multisample renderbuffer.

**Note:** the resulting :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` does not own any native resources, it merely contains references and the associated metadata of the size and sample count. It is the caller's responsibility to ensure that the native resource exists as long as necessary.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.
