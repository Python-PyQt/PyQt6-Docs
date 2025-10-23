.. sip:class-description::
    :status: todo
    :brief: Information about available multimedia input and output devices
    :digest: 481c7fe06a420b7f520b46a8f210d4a1

The :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` class provides information about available multimedia input and output devices.

The :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` class provides information about the available multimedia devices and the system defaults. It monitors the following three groups:

* Audio input devices (Microphones)

* Audio output devices (Speakers, Headsets)

* Video input devices (Cameras)

:sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` provides a separate list for each device group. If it detects that a new device has been connected to the system or an attached device has been disconnected from the system, it will update the corresponding device list and emit a signal notifying about the change.

The :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.audioInputs` and :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.audioOutputs` functions can be used to enumerate all microphones and speakers/headsets on the system. This example first gets a list of all connected microphones, and then prints their identifier, description, and if it is the default device or not.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-devices.py
    :lines: 20-26

Similarly, the :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.videoInputs` will return a list of all connected cameras. In this example we list all connected cameras and their identifier, description, and if it is the default camera or not.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-devices.py
    :lines: 30-36

:sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` monitors the system defaults for each device group. It will notify about any changes done through the system settings. For example, if the user selects a new default audio output in the system settings, :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` will update the default audio output accordingly and emit a signal. If the system does not provide a default for a camera or an audio input, :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` will select the first device from the list as the default device.

While using the default input and output devices is often sufficient for playing back or recording multimedia, there is often a need to explicitly select the device to be used.

:sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` is a singleton object and all getters are thread-safe.

**Note:** On WebAssembly platform, due to it's asynchronous nature, the lists of devices will only be available after :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.audioInputsChanged`, audioOutputsChanded, or :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.videoInputsChanged` notifications.
