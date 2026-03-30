.. sip:method-description::
    :status: todo
    :pysig: d6a2e82ecf3e8c8131ecdc0e3f88a67c
    :realsig: (const QByteArray&)
    :digest: 917ecafbce6e8f28222ff803fc82b9b4

Creates a :sip:ref:`~PyQt6.QtGui.QColorSpace` from ICC profile *iccProfile*.

**Note:** Not all ICC profiles are supported. :sip:ref:`~PyQt6.QtGui.QColorSpace` only supports RGB or Gray ICC profiles.

If the ICC profile is not supported an invalid :sip:ref:`~PyQt6.QtGui.QColorSpace` is returned where you can still read the original ICC profile using :sip:ref:`~PyQt6.QtGui.QColorSpace.iccProfile`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColorSpace.iccProfile`.
