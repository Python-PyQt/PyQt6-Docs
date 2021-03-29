.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 044b8dcd551653c64069f4b33a5bcf59

This virtual handler is called when a button is clicked. The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setChecked`\ (!\ :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isChecked`) if the button :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isCheckable`. It allows subclasses to implement intermediate button states.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.checkStateSet`.
