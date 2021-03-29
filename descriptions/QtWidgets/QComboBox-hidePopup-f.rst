.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 72c0994164b3eeaf42082730b596e5d3

Hides the list of items in the combobox if it is currently visible and resets the internal state, so that if the custom pop-up was shown inside the reimplemented :sip:ref:`~PyQt6.QtWidgets.QComboBox.showPopup`, then you also need to reimplement the  function to hide your custom pop-up and call the base class implementation to reset the internal state whenever your custom pop-up widget is hidden.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.showPopup`.
