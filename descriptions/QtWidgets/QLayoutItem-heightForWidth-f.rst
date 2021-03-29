.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: ae3d97952ec9ac8eb0fe3825ab599244

Returns the preferred height for this layout item, given the width, which is not used in this default implementation.

The default implementation returns -1, indicating that the preferred height is independent of the width of the item. Using the function :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.hasHeightForWidth` will typically be much faster than calling this function and testing for -1.

Reimplement this function in layout managers that support height for width. A typical implementation will look like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qlayoutitem.py
    :lines: 54-63

Caching is strongly recommended; without it layout will take exponential time.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.hasHeightForWidth`.
