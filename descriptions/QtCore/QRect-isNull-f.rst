.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 4a088f0454d86cc735de5cfaada56320

Returns ``true`` if the rectangle is a null rectangle, otherwise returns ``false``.

A null rectangle has both the width and the height set to 0 (i.e., :sip:ref:`~PyQt6.QtCore.QRect.right` == :sip:ref:`~PyQt6.QtCore.QRect.left` - 1 and :sip:ref:`~PyQt6.QtCore.QRect.bottom` == :sip:ref:`~PyQt6.QtCore.QRect.top` - 1). A null rectangle is also empty, and hence is not valid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.isEmpty`, :sip:ref:`~PyQt6.QtCore.QRect.isValid`.
