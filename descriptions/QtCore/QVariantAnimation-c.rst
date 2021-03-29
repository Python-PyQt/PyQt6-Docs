.. sip:class-description::
    :status: todo
    :brief: Base class for animations
    :digest: 27c1d4d2f2e02d17284acfcedd431c1a

The :sip:ref:`~PyQt6.QtCore.QVariantAnimation` class provides a base class for animations.

This class is part of `The Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_. It serves as a base class for property and item animations, with functions for shared functionality.

The class performs interpolation over `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_s, but leaves using the interpolated values to its subclasses. Currently, Qt provides :sip:ref:`~PyQt6.QtCore.QPropertyAnimation`, which animates Qt `properties <https://doc.qt.io/qt-6/properties.html>`_. See the :sip:ref:`~PyQt6.QtCore.QPropertyAnimation` class description if you wish to animate such properties.

You can then set start and end values for the property by calling :sip:ref:`~PyQt6.QtCore.QVariantAnimation.setStartValue` and :sip:ref:`~PyQt6.QtCore.QVariantAnimation.setEndValue`, and finally call start() to start the animation. :sip:ref:`~PyQt6.QtCore.QVariantAnimation` will interpolate the property of the target object and emit :sip:ref:`~PyQt6.QtCore.QVariantAnimation.valueChanged`. To react to a change in the current value you have to reimplement the :sip:ref:`~PyQt6.QtCore.QVariantAnimation.updateCurrentValue` virtual function or connect to said signal.

It is also possible to set values at specified steps situated between the start and end value. The interpolation will then touch these points at the specified steps. Note that the start and end values are defined as the key values at 0.0 and 1.0.

There are two ways to affect how :sip:ref:`~PyQt6.QtCore.QVariantAnimation` interpolates the values. You can set an easing curve by calling :sip:ref:`~PyQt6.QtCore.QVariantAnimation.setEasingCurve`, and configure the duration by calling :sip:ref:`~PyQt6.QtCore.QVariantAnimation.setDuration`. You can change how the `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_s are interpolated by creating a subclass of :sip:ref:`~PyQt6.QtCore.QVariantAnimation`, and reimplementing the virtual :sip:ref:`~PyQt6.QtCore.QVariantAnimation.interpolated` function.

Subclassing :sip:ref:`~PyQt6.QtCore.QVariantAnimation` can be an alternative if you have `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_s that you do not wish to declare as Qt properties. Note, however, that you in most cases will be better off declaring your `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ as a property.

Not all `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ types are supported. Below is a list of currently supported `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ types:

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Int`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.UInt`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Double`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Float`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QLine`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QLineF`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QPoint`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QPointF`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QSize`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QSizeF`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QRect`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QRectF`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QColor`

If you need to interpolate other variant types, including custom types, you have to implement interpolation for these yourself. To do this, you can register an interpolator function for a given type. This function takes 3 parameters: the start value, the end value, and the current progress.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_animation_qvariantanimation.py
    :lines: 54-60

Another option is to reimplement :sip:ref:`~PyQt6.QtCore.QVariantAnimation.interpolated`, which returns interpolation values for the value being interpolated.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPropertyAnimation`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`, `The Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_.
