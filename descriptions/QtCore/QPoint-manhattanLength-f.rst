.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 1c2fd1709cb514ba8e9e0d4af502fc8b

Returns the sum of the absolute values of :sip:ref:`~PyQt6.QtCore.QPoint.x` and :sip:ref:`~PyQt6.QtCore.QPoint.y`, traditionally known as the "Manhattan length" of the vector from the origin to the point. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qpoint.py
    :lines: 108-115

This is a useful, and quick to calculate, approximation to the true length:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qpoint.py
    :lines: 120-120

The tradition of "Manhattan length" arises because such distances apply to travelers who can only travel on a rectangular grid, like the streets of Manhattan.
