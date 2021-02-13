.. sip:method-description::
    :status: todo
    :pysig: de0a3803cf0933020b7b3fc85f9f7085
    :realsig: (QSizePolicy::ControlType)
    :digest: fff57c468c3b7bb34c16c02b3ad52b07

Sets the control type associated with the widget for which this size policy applies to *type*.

The control type specifies the type of the widget for which this size policy applies. It is used by some styles, notably QMacStyle, to insert proper spacing between widgets. For example, the macOS Aqua guidelines specify that push buttons should be separated by 12 pixels, whereas vertically stacked radio buttons only require 6 pixels.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.controlType`, :sip:ref:`~PyQt6.QtWidgets.QStyle.layoutSpacing`.
