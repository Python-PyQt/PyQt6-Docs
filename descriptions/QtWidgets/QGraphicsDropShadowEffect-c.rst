.. sip:class-description::
    :status: todo
    :brief: Drop shadow effect
    :digest: 66894050ddb3d448dd20fdf1a82a41a5

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsDropShadowEffect` class provides a drop shadow effect.

A drop shadow effect renders the source with a drop shadow. The color of the drop shadow can be modified using the :sip:ref:`~PyQt6.QtWidgets.QGraphicsDropShadowEffect.setColor` function. The drop shadow offset can be modified using the :sip:ref:`~PyQt6.QtWidgets.QGraphicsDropShadowEffect.setOffset` function and the blur radius of the drop shadow can be changed with the :sip:ref:`~PyQt6.QtWidgets.QGraphicsDropShadowEffect.setBlurRadius` function.

By default, the drop shadow is a semi-transparent dark gray (\ :sip:ref:`~PyQt6.QtGui.QColor`\ (63, 63, 63, 180)) shadow, blurred with a radius of 1 at an offset of 8 pixels towards the lower right. The drop shadow offset is specified in device coordinates.

.. image:: ../../../images/graphicseffect-drop-shadow.png

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsBlurEffect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsColorizeEffect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsOpacityEffect`.
