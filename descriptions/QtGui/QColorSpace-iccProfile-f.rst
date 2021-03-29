.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 3dbc462b4fbb8aed63b91e18a57c0f3e

Returns an ICC profile representing the color space.

If the color space was generated from an ICC profile, that profile is returned, otherwise one is generated.

**Note:** Even invalid color spaces may return the ICC profile if they were generated from one, to allow applications to implement wider support themselves.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColorSpace.fromIccProfile`.
