.. sip:method-description::
    :status: todo
    :pysig: 1035e71011e4d1cb0e076e15c2d0bdd9
    :realsig: () const
    :digest: 853daa40ab349b94c96950f9ce03829a

Virtual function that determines whether stepping up and down is legal at any given time.

The up arrow will be painted as disabled unless (stepEnabled() & :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.StepEnabled.StepUpEnabled`) != 0.

The default implementation will return (\ :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.StepEnabled.StepUpEnabled`| :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.StepEnabled.StepDownEnabled`) if wrapping is turned on. Else it will return :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.StepEnabled.StepDownEnabled` if value is > minimum() or'ed with :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.StepEnabled.StepUpEnabled` if value < maximum().

If you subclass :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` you will need to reimplement this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSpinBox.minimum`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox.maximum`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.wrapping`.
