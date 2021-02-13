.. sip:method-description::
    :status: todo
    :pysig: e2f30f15892513e79f819481b5672312
    :realsig: (QAbstractSlider::SliderChange)
    :digest: 5e5a42a95f32fb12b1da9c0b6b88f31f

Reimplement this virtual function to track slider changes such as :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderRangeChange`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderOrientationChange`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderStepsChange`, or :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderValueChange`. The default implementation only updates the display and ignores the *change* parameter.
