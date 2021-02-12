.. sip:class-description::
    :status: todo
    :brief: Easing curves for controlling animation
    :digest: 7c60012f36640fa4aac7adc653dba68e

The :sip:ref:`~PyQt6.QtCore.QEasingCurve` class provides easing curves for controlling animation.

Easing curves describe a function that controls how the speed of the interpolation between 0 and 1 should be. Easing curves allow transitions from one value to another to appear more natural than a simple constant speed would allow. The :sip:ref:`~PyQt6.QtCore.QEasingCurve` class is usually used in conjunction with the :sip:ref:`~PyQt6.QtCore.QVariantAnimation` and :sip:ref:`~PyQt6.QtCore.QPropertyAnimation` classes but can be used on its own. It is usually used to accelerate the interpolation from zero velocity (ease in) or decelerate to zero velocity (ease out). Ease in and ease out can also be combined in the same easing curve.

To calculate the speed of the interpolation, the easing curve provides the function :sip:ref:`~PyQt6.QtCore.QEasingCurve.valueForProgress`, where the *progress* argument specifies the progress of the interpolation: 0 is the start value of the interpolation, 1 is the end value of the interpolation. The returned value is the effective progress of the interpolation. If the returned value is the same as the input value for all input values the easing curve is a linear curve. This is the default behaviour.

For example,

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qeasingcurve.py
    :lines: 58-62

will print the effective progress of the interpolation between 0 and 1.

When using a :sip:ref:`~PyQt6.QtCore.QPropertyAnimation`, the associated easing curve will be used to control the progress of the interpolation between startValue and endValue:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qeasingcurve.py
    :lines: 66-70

The ability to set an amplitude, overshoot, or period depends on the :sip:ref:`~PyQt6.QtCore.QEasingCurve` type. Amplitude access is available to curves that behave as springs such as elastic and bounce curves. Changing the amplitude changes the height of the curve. Period access is only available to elastic curves and setting a higher period slows the rate of bounce. Only curves that have "boomerang" behaviors such as the :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.InBack`, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.OutBack`, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.InOutBack`, and :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.OutInBack` have overshoot settings. These curves will interpolate beyond the end points and return to the end point, acting similar to a boomerang.

The Easing Curves Example contains samples of :sip:ref:`~PyQt6.QtCore.QEasingCurve` types and lets you change the curve settings.
