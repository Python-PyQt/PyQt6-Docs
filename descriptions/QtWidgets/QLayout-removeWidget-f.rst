.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 5f6728f27c53b2b0706faf7d60e0c5a0

Removes the widget *widget* from the layout. After this call, it is the caller's responsibility to give the widget a reasonable geometry or to put the widget back into a layout or to explicitly hide it if necessary.

**Note:** The ownership of *widget* remains the same as when it was added.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayout.removeItem`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setGeometry`, :sip:ref:`~PyQt6.QtWidgets.QLayout.addWidget`.
