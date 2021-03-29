.. sip:method-description::
    :status: todo
    :pysig: 35f2abd91a1c7c0f976e61da95cebf96
    :realsig: (QHideEvent*)
    :digest: 61cd3dfa5543dd4d5ac977dc572bcd69

This event handler can be reimplemented in a subclass to receive widget hide events. The event is passed in the *event* parameter.

Hide events are sent to widgets immediately after they have been hidden.

Note: A widget receives spontaneous show and hide events when its mapping status is changed by the window system, e.g. a spontaneous hide event when the user minimizes the window, and a spontaneous show event when the window is restored again. After receiving a spontaneous hide event, a widget is still considered visible in the sense of :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`.

.. seealso:: visible, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QHideEvent`.
