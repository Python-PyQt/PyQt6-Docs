.. sip:enum-member-description::
    :status: todo
    :value: 120
    :digest: 990a6867084107bcbfcb0229824ddfba

Indicates that the widget should have a translucent background, i.e., any non-opaque regions of the widgets will be translucent because the widget will have an alpha channel. Setting this flag causes  to be set. On Windows the widget also needs the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.FramelessWindowHint` window flag to be set. This flag is set or cleared by the widget's author.
