.. sip:class-description::
    :status: todo
    :brief: Information about available multimedia input and output devices
    :digest: 2e1d6a031df753e3eb6c5732c257a397

The :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` class provides information about available multimedia input and output devices.

The :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` class provides information about the available multimedia devices and the system defaults. It monitors the following three groups:

* Audio input devices (Microphones)

* Audio output devices (Speakers, Headsets)

* Video input devices (Cameras)

:sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` provides a separate list for each device group. If it detects that a new device has been connected to the system or an attached device has been disconnected from the system, it will update the corresponding device list and emit a signal notifying about the change.

:sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` monitors the system defaults for each device group. It will notify about any changes done through the system settings. For example, if the user selects a new default audio output in the system settings, :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` will update the default audio output accordingly and emit a signal. If the system does not provide a default for a camera or an audio input, :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` will select the first device from the list as the default device.

While using the default input and output devices is often sufficient for playing back or recording multimedia, there is often a need to explicitly select the device to be used.

:sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` is a singleton object and all getters are thread-safe.
