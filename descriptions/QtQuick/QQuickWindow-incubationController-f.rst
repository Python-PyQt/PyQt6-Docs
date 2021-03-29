.. sip:method-description::
    :status: todo
    :pysig: ce021580b00d6672f51139a1cc4046a7
    :realsig: () const
    :digest: f77100fbc8969f98b518eceafe8f83ad

Returns an incubation controller that splices incubation between frames for this window. :sip:ref:`~PyQt6.QtQuick.QQuickView` automatically installs this controller for you, otherwise you will need to install it yourself using :sip:ref:`~PyQt6.QtQml.QQmlEngine.setIncubationController`.

The controller is owned by the window and will be destroyed when the window is deleted.
