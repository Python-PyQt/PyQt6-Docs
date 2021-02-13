.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: ca69b2d27e1c1edcc14a9ac332347232

The :sip:ref:`~PyQt6.QtCore.QEasingCurve` used when decelerating the scrolling velocity after an user initiated flick. Please note that this is the easing curve for the positions, **not** the velocity: the default is :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.OutQuad`, which results in a linear decrease in velocity (1st derivative) and a constant deceleration (2nd derivative).
