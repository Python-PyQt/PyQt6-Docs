.. sip:class-description::
    :status: todo
    :brief: Rounded range control (like a speedometer or potentiometer)
    :digest: 91050437f6c3c7c1545c5d5f33f4394d

The :sip:ref:`~PyQt6.QtWidgets.QDial` class provides a rounded range control (like a speedometer or potentiometer).

.. image:: ../../../images/windows-dial.png

:sip:ref:`~PyQt6.QtWidgets.QDial` is used when the user needs to control a value within a program-definable range, and the range either wraps around (for example, with angles measured from 0 to 359 degrees) or the dialog layout needs a square widget.

Since :sip:ref:`~PyQt6.QtWidgets.QDial` inherits from :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider`, the dial behaves in a similar way to a :sip:ref:`~PyQt6.QtWidgets.QSlider`. When :sip:ref:`~PyQt6.QtWidgets.QDial.wrapping` is false (the default setting) there is no real difference between a slider and a dial. They both share the same signals, slots and member functions. Which one you use depends on the expectations of your users and on the type of application.

The dial initially emits valueChanged() signals continuously while the slider is being moved; you can make it emit the signal less often by disabling the tracking property. The sliderMoved() signal is emitted continuously even when tracking is disabled.

The dial also emits sliderPressed() and sliderReleased() signals when the mouse button is pressed and released. Note that the dial's value can change without these signals being emitted since the keyboard and wheel can also be used to change the value.

Unlike the slider, :sip:ref:`~PyQt6.QtWidgets.QDial` attempts to draw a "nice" number of notches rather than one per line step. If possible, the number of notches drawn is one per line step, but if there aren't enough pixels to draw every one, :sip:ref:`~PyQt6.QtWidgets.QDial` will skip notches to try and draw a uniform set (e.g. by drawing every second or third notch).

Like the slider, the dial makes the :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider` function setValue() available as a slot.

The dial's keyboard interface is fairly simple: The left/up and right/down arrow keys adjust the dial's :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.value` by the defined :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.singleStep`, Page Up and Page Down by the defined :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.pageStep`, and the Home and End keys set the value to the defined :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.minimum` and :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.maximum` values.

If you are using the mouse wheel to adjust the dial, the increment value is determined by the lesser value of :sip:ref:`~PyQt6.QtWidgets.QApplication.wheelScrollLines` multipled by :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.singleStep`, and :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.pageStep`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScrollBar`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QSlider`, `GUI Design Handbook: Slider <https://doc.qt.io/qt-6/guibooks.html#fowler>`_, `Sliders Example <https://doc.qt.io/qt-6/qtwidgets-widgets-sliders-example.html>`_.
