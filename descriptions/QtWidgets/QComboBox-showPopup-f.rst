.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c8f72380a04769d4a01a602fa9368312

Displays the list of items in the combobox. If the list is empty then no items will be shown.

If you reimplement this function to show a custom pop-up, make sure you call :sip:ref:`~PyQt6.QtWidgets.QComboBox.hidePopup` to reset the internal state.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.hidePopup`.
