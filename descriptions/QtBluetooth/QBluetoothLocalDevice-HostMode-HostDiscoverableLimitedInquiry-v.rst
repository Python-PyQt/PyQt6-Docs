.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: 64068dc3b03ede8d8e36c7c9fa9f1867

Remote Bluetooth devices can discover the presence of the local Bluetooth device when performing a limited inquiry. This should be used for locating services that are only made discoverable for a limited period of time. This can speed up discovery between gaming devices, as service discovery can be skipped on devices not in LimitedInquiry mode. In this mode, the device will be connectable and powered on, if required. This mode is is not supported on Android.
