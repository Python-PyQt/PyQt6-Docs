.. sip:method-description::
    :status: todo
    :pysig: a809066194c68e595c18fee038a13409
    :realsig: () const
    :digest: bbe045209b121a82f841b79972fda137

Returns the tag of the axis. This is a four-character sequence which identifies the axis. Certain tags have standardized meanings, such as "wght" (weight) and "wdth" (width), but any sequence of four latin-1 characters is a valid tag. By convention, non-standard/custom axes are denoted by tags in all uppercase.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontVariableAxis.setTag`, :sip:ref:`~PyQt6.QtGui.QFont.setVariableAxis`, :sip:ref:`~PyQt6.QtGui.QFontVariableAxis.name`.
