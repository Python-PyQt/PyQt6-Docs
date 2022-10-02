.. sip:enum-description::
    :status: todo
    :digest: aa4c61318d1c3c89b3f9993e17705fa2

This enum is used to specify the OpenGL context profile, in conjunction with :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setMajorVersion` and :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setMinorVersion`.

Profiles are exposed in OpenGL 3.2 and above, and are used to choose between a restricted core profile, and a compatibility profile which might contain deprecated support functionality.

Note that the core profile might still contain functionality that is deprecated and scheduled for removal in a higher version. To get access to the deprecated functionality for the core profile in the set OpenGL version you can use the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` format option :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.FormatOption.DeprecatedFunctions`.
