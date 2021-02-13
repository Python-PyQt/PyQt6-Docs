.. sip:method-description::
    :status: todo
    :pysig: 0f9b0ea7a3407ca50e1df7b110b9ad1f
    :realsig: (const QString&) const
    :digest: d27f60e098524b0b2692a9f74440f950

This virtual function is used by the spin box whenever it needs to interpret *text* entered by the user as a value.

Subclasses that need to display spin box values in a non-numeric way need to reimplement this function.

Note: :sip:ref:`~PyQt6.QtWidgets.QSpinBox` handles specialValueText() separately; this function is only concerned with the other values.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSpinBox.textFromValue`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox.validate`.
