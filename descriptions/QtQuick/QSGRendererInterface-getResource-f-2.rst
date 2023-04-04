.. sip:method-description::
    :status: todo
    :pysig: 56190ef564fb6146ff43713cd87676e0
    :realsig: (QQuickWindow*,QSGRendererInterface::Resource) const
    :digest: a077606abe5a8c01c99707d74083b06e

Queries a graphics *resource* in *window*. Returns null when the resource in question is not supported or not available.

When successful, the returned pointer is either a direct pointer to an interface, or a pointer to an opaque handle that needs to be dereferenced first (for example, ``VkDevice dev = \*static_cast<VkDevice \*>(result)``). The latter is necessary since such handles may have sizes different from a pointer.

**Note:** The ownership of the returned pointer is never transferred to the caller.

**Note:** This function must only be called on the render thread.
