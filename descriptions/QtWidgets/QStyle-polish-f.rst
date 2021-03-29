.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 6a202e473ffc92a282294b2189f23a13

Initializes the appearance of the given *widget*.

This function is called for every widget at some point after it has been fully created but just *before* it is shown for the very first time.

Note that the default implementation does nothing. Reasonable actions in this function might be to call the QWidget::setBackgroundMode() function for the widget. Do not use the function to set, for example, the geometry. Reimplementing this function provides a back-door through which the appearance of a widget can be changed, but with Qt's style engine it is rarely necessary to implement this function; reimplement :sip:ref:`~PyQt6.QtWidgets.QStyle.drawItemPixmap`, :sip:ref:`~PyQt6.QtWidgets.QStyle.drawItemText`, :sip:ref:`~PyQt6.QtWidgets.QStyle.drawPrimitive`, etc. instead.

The QWidget::inherits() function may provide enough information to allow class-specific customizations. But because new :sip:ref:`~PyQt6.QtWidgets.QStyle` subclasses are expected to work reasonably with all current and *future* widgets, limited use of hard-coded customization is recommended.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle.unpolish`.
