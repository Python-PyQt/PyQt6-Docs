.. sip:method-description::
    :status: todo
    :pysig: 2999588c832aa40c83738291cf2f3c9c
    :realsig: (const QByteArray&)
    :digest: 917ecafbce6e8f28222ff803fc82b9b4

Creates a :sip:ref:`~PyQt6.QtGui.QColorSpace` from ICC profile *iccProfile*.

**Note:** Not all ICC profiles are supported. :sip:ref:`~PyQt6.QtGui.QColorSpace` only supports RGB-XYZ ICC profiles that are three-component matrix-based.

If the ICC profile is not supported an invalid :sip:ref:`~PyQt6.QtGui.QColorSpace` is returned where you can still read the original ICC profile using :sip:ref:`~PyQt6.QtGui.QColorSpace.iccProfile`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColorSpace.iccProfile`.
