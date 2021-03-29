.. sip:method-description::
    :status: todo
    :pysig: 9d5f3afb9455bc798ab36f723ee8cbf1
    :realsig: (const QMetaMethod&) const
    :digest: 4651e2b7e037db3dbd9ab8b81cd11e12

Returns ``true`` if the *signal* is connected to at least one receiver, otherwise returns ``false``.

*signal* must be a signal member of this object, otherwise the behaviour is undefined.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 489-494

As the code snippet above illustrates, you can use this function to avoid emitting a signal that nobody listens to.

**Warning:** This function violates the object-oriented principle of modularity. However, it might be useful when you need to perform expensive initialization only if something is connected to a signal.
