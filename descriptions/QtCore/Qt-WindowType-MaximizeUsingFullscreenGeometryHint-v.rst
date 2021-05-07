.. sip:enum-member-description::
    :status: todo
    :value: 0x00400000
    :digest: 3a0d37504b79cfdcdf2286a81985748f

Informs the window system that when maximizing the window it should use as much of the available screen geometry as possible, including areas that may be covered by system UI such as status bars or application launchers. This may result in the window being placed under these system UIs, but does not guarantee it, depending on whether or not the platform supports it. When the flag is enabled the user is responsible for taking :sip:ref:`~PyQt6.QtGui.QScreen.availableGeometry` into account, so that any UI elements in the application that require user interaction are not covered by system UI.
