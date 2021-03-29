.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 90d42bae83935d34418cf8c351626384

This function is called from ``addWidget()`` functions in subclasses to add *w* as a managed widget of a layout.

If *w* is already managed by a layout, this function will give a warning and remove *w* from that layout. This function must therefore be called before adding *w* to the layout's data structure.
