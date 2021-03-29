.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 781d2ed85baa939b8203cbbe445d43e9

Performs an animated click: the button is pressed immediately, and released 100ms later.

Calling this function again before the button is released resets the release timer.

All signals associated with a click are emitted as appropriate.

This function does nothing if the button is disabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.click`.
