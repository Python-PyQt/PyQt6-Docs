.. sip:enum-member-description::
    :status: todo
    :value: 5
    :digest: 5100881b3080045ee11de731aad86b9c

Indicates that Qt is used to author a plugin. Depending on the operating system, it suppresses specific initializations that do not necessarily make sense in the plugin case. For example on macOS, this includes avoiding loading our nib for the main menu and not taking possession of the native menu bar. Setting this attribute to true will also set the  attribute to true. It also disables native event filters. This attribute must be set before :sip:ref:`~PyQt6.QtGui.QGuiApplication` constructed. This value was added in Qt 5.7.
