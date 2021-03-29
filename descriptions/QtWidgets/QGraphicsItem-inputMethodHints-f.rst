.. sip:method-description::
    :status: todo
    :pysig: 319e0dbb6ea5cb8ffc22b15cae31069b
    :realsig: () const
    :digest: 09b8714463ebdf8ce82fb84f4159bf16

Returns the current input method hints of this item.

Input method hints are only relevant for input items. The hints are used by the input method to indicate how it should operate. For example, if the Qt::ImhNumbersOnly flag is set, the input method may change its visual components to reflect that only numbers can be entered.

The effect may vary between input method implementations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setInputMethodHints`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.inputMethodQuery`.
