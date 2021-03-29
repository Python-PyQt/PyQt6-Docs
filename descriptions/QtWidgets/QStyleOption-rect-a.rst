.. sip:attribute-description::
    :status: todo
    :digest: 8b5cef3b9616b2cddd98d21188fb137c

This variable holds the area that should be used for various calculations and painting.

This can have different meanings for different types of elements. For example, for a :sip:ref:`~PyQt6.QtWidgets.QStyle.ControlElement.CE_PushButton` element it would be the rectangle for the entire button, while for a :sip:ref:`~PyQt6.QtWidgets.QStyle.ControlElement.CE_PushButtonLabel` element it would be just the area for the push button label.

The default value is a null rectangle, i.e. a rectangle with both the width and the height set to 0.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption.initFrom`.
