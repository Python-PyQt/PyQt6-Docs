.. sip:method-description::
    :status: todo
    :pysig: fe16b9ee4a375a9a3a3b8330a3aef226
    :realsig: (const QString&) const
    :digest: 7e7902f8f4be38a365a04d9d75b61e17

This virtual function is used by the spin box whenever it needs to interpret *text* entered by the user as a value.

Subclasses that need to display spin box values in a non-numeric way need to reimplement this function.

Note: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` handles specialValueText() separately; this function is only concerned with the other values.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.textFromValue`, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.validate`.
