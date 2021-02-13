.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 1b0a89c52485fa507a67ef0265438497

Returns ``true`` if the widget is hidden, otherwise returns ``false``.

A hidden widget will only become visible when :sip:ref:`~PyQt6.QtWidgets.QWidget.show` is called on it. It will not be automatically shown when the parent is shown.

To check visibility, use !\ :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible` instead (notice the exclamation mark).

implies !\ :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`, but a widget can be not visible and not hidden at the same time. This is the case for widgets that are children of widgets that are not visible.

Widgets are hidden if:

* they were created as independent windows,

* they were created as children of visible widgets,

* :sip:ref:`~PyQt6.QtWidgets.QWidget.hide` or :sip:ref:`~PyQt6.QtWidgets.QWidget.setVisible`\ (false) was called.
