.. sip:attribute-description::
    :status: todo
    :digest: 2855e55dbf503741b0596adc0b591431

This variable holds a version corresponding to macOS Big Sur.

The actual version number depends on whether the application was built using the Xcode 12 SDK. If it was, the version number corresponds to macOS 11.0. If not it will correspond to macOS 10.16.

By comparing :sip:ref:`~PyQt6.QtCore.QOperatingSystemVersion.current` to this constant you will always end up comparing to the right version number.
