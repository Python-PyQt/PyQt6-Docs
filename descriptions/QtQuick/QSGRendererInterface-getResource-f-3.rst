.. sip:method-description::
    :status: todo
    :pysig: 22033b5f3fea4da847f0cce73f24a458
    :realsig: (QQuickWindow*,const char*) const
    :digest: 88afaf8c1f16eea086c8125d0a7a5803

Queries a graphics resource. *resource* is a backend-specific key. This allows supporting any future resources that are not listed in the Resource enum.

**Note:** The ownership of the returned pointer is never transferred to the caller.

**Note:** This function must only be called on the render thread.
