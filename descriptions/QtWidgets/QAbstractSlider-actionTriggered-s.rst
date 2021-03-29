.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: caa8a9e071ff90d1de67d3a87f06ec06

This signal is emitted when the slider action *action* is triggered. Actions are :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderSingleStepAdd`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderSingleStepSub`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderPageStepAdd`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderPageStepSub`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderToMinimum`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderToMaximum`, and :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderMove`.

When the signal is emitted, the :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderPosition` has been adjusted according to the action, but the :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.value` has not yet been propagated (meaning the :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.valueChanged` signal was not yet emitted), and the visual display has not been updated. In slots connected to this signal you can thus safely adjust any action by calling :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.setSliderPosition` yourself, based on both the action and the slider's value.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.triggerAction`.
