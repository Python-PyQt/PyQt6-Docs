.. sip:method-description::
    :status: todo
    :pysig: 1cb55db74c689c678d9d6e1d477fe870
    :realsig: (QAbstractSpinBox::StepType)
    :digest: 5c6ea7128d9c8c1f2b6dcadde4be031b

Sets the step type for the spin box to *stepType*, which is single step or adaptive decimal step.

Adaptive decimal step means that the step size will continuously be adjusted to one power of ten below the current :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.value`. So when the value is 1100, the step is set to 100, so stepping up once increases it to 1200. For 1200 stepping up takes it to 1300. For negative values, stepping down from -1100 goes to -1200.

It also works for any decimal values, 0.041 is increased to 0.042 by stepping once.

Step direction is taken into account to handle edges cases, so that stepping down from 100 takes the value to 99 instead of 90. Thus a step up followed by a step down – or vice versa – always lands on the starting value; 99 -> 100 -> 99.

Setting this will cause the spin box to disregard the value of :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.singleStep`, although it is preserved so that :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.singleStep` comes into effect if adaptive decimal step is later turned off.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.stepType`.
