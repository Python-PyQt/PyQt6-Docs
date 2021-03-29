.. sip:method-description::
    :status: todo
    :pysig: 7905de75ba1096b008e853dc1ed418eb
    :realsig: (QShowEvent*)
    :digest: f3f796442e5caa8fdb09bd19b2742ff8

This event handler can be reimplemented in a subclass to receive widget show events which are passed in the *event* parameter.

Non-spontaneous show events are sent to widgets immediately before they are shown. The spontaneous show events of windows are delivered afterwards.

Note: A widget receives spontaneous show and hide events when its mapping status is changed by the window system, e.g. a spontaneous hide event when the user minimizes the window, and a spontaneous show event when the window is restored again. After receiving a spontaneous hide event, a widget is still considered visible in the sense of :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`.

.. seealso:: visible, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QShowEvent`.
