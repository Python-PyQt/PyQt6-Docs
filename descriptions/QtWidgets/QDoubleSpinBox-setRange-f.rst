.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (double,double)
    :digest: 654c784cee5122b0d53531b288da4218

Convenience function to set the *minimum* and *maximum* values with a single function call.

Note: The maximum and minimum values will be rounded to match the decimals property.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qspinbox.py
    :lines: 85-85

is equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qspinbox.py
    :lines: 90-91

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.minimum`, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.maximum`.
