.. sip:class-description::
    :status: todo
    :brief: Integer value within a range
    :digest: 3ba2fb0da4ecefd988b834090900e956

The :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider` class provides an integer value within a range.

The class is designed as a common super class for widgets like :sip:ref:`~PyQt6.QtWidgets.QScrollBar`, :sip:ref:`~PyQt6.QtWidgets.QSlider` and :sip:ref:`~PyQt6.QtWidgets.QDial`.

Here are the main properties of the class:

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.value`: The bounded integer that :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider` maintains.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.minimum`: The lowest possible value.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.maximum`: The highest possible value.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.singleStep`: The smaller of two natural steps that an abstract sliders provides and typically corresponds to the user pressing an arrow key.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.pageStep`: The larger of two natural steps that an abstract slider provides and typically corresponds to the user pressing PageUp or PageDown.

#. tracking: Whether slider tracking is enabled.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderPosition`: The current position of the slider. If tracking is enabled (the default), this is identical to :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.value`.

Unity (1) may be viewed as a third step size. :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.setValue` lets you set the current value to any integer in the allowed range, not just :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.minimum` + *n* \* :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.singleStep` for integer values of *n*. Some widgets may allow the user to set any value at all; others may just provide multiples of :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.singleStep` or :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.pageStep`.

:sip:ref:`~PyQt6.QtWidgets.QAbstractSlider` emits a comprehensive set of signals:

+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Signal                                                      | Emitted when                                                                                           |
+=============================================================+========================================================================================================+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.valueChanged`    | the value has changed. The tracking determines whether this signal is emitted during user interaction. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderPressed`   | the user starts to drag the slider.                                                                    |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderMoved`     | the user drags the slider.                                                                             |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderReleased`  | the user releases the slider.                                                                          |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.actionTriggered` | a slider action was triggerd.                                                                          |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.rangeChanged`    | a the range has changed.                                                                               |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

:sip:ref:`~PyQt6.QtWidgets.QAbstractSlider` provides a virtual :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderChange` function that is well suited for updating the on-screen representation of sliders. By calling :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.triggerAction`, subclasses trigger slider actions. Two helper functions :sip:ref:`~PyQt6.QtWidgets.QStyle.sliderPositionFromValue` and :sip:ref:`~PyQt6.QtWidgets.QStyle.sliderValueFromPosition` help subclasses and styles to map screen coordinates to logical range values.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QSlider`, :sip:ref:`~PyQt6.QtWidgets.QDial`, :sip:ref:`~PyQt6.QtWidgets.QScrollBar`, `Sliders Example <https://doc.qt.io/qt-6/qtwidgets-widgets-sliders-example.html>`_.
