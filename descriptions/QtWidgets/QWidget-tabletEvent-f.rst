.. sip:method-description::
    :status: todo
    :pysig: 0045cdeec65d90d8dc28c97781cd0172
    :realsig: (QTabletEvent*)
    :digest: 7f14a5dd4e1f5fc6c766d3e8b6e30951

This event handler, for event *event*, can be reimplemented in a subclass to receive tablet events for the widget.

If you reimplement this handler, it is very important that you :sip:ref:`~PyQt6.QtCore.QEvent` the event if you do not handle it, so that the widget's parent can interpret it.

The default implementation ignores the event.

If tablet tracking is switched off, tablet move events only occur if the stylus is in contact with the tablet, or at least one stylus button is pressed, while the stylus is being moved. If tablet tracking is switched on, tablet move events occur even while the stylus is hovering in proximity of the tablet, with no buttons pressed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEvent.ignore`, :sip:ref:`~PyQt6.QtCore.QEvent.accept`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setTabletTracking`, :sip:ref:`~PyQt6.QtGui.QTabletEvent`.
