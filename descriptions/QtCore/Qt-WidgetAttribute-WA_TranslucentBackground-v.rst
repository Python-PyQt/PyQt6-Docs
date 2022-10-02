.. sip:enum-member-description::
    :status: todo
    :value: 120
    :digest: 5ee1e6c434f170fec9b691ae8ca68028

Indicates that the widget should have a translucent background, i.e., any non-opaque regions of the widgets will be translucent because the widget will have an alpha channel. Setting this flag causes WA_NoSystemBackground to be set. On Windows the widget also needs the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.FramelessWindowHint` window flag to be set. This flag is set or cleared by the widget's author. As of Qt 5.0, toggling this attribute after the widget has been shown is not uniformly supported across platforms. When translucent background is desired, set the attribute early when creating the widget, and avoid altering it afterwards.
