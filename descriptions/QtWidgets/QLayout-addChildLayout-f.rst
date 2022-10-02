.. sip:method-description::
    :status: todo
    :pysig: 2f0da4d3658dfe115217ca868dfa5e64
    :realsig: (QLayout*)
    :digest: 1205deca922d85fd41c0bb61de669f77

This function is called from ``addLayout()`` or ``insertLayout()`` functions in subclasses to add layout *childLayout* as a sub-layout.

The only scenario in which you need to call it directly is if you implement a custom layout that supports nested layouts.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addLayout`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertLayout`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addLayout`.
