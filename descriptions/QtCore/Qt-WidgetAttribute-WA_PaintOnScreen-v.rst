.. sip:enum-member-description::
    :status: todo
    :value: 8
    :digest: f84ed46206b741ae23283fd0140020ca

Indicates that the widget wants to draw directly onto the screen. Widgets with this attribute set do not participate in composition management, i.e. they cannot be semi-transparent or shine through semi-transparent overlapping widgets. **Note**: This flag is only supported on X11 and it disables double buffering. On Qt for Embedded Linux, the flag only works when set on a top-level widget and it relies on support from the active screen driver. This flag is set or cleared by the widget's author. To render outside of Qt's paint system, e.g., if you require native painting primitives, you need to reimplement :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEngine` to return 0 and set this flag.
