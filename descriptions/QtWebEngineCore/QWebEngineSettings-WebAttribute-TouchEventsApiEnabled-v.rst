.. sip:enum-member-description::
    :status: todo
    :value: 36
    :digest: e52edc2b97ef12b3778dc1b87f9a40d0

Enables support for JavaScript touch events API, meaning ``ontouchstart``, ``ontouchend`` and ``ontouchmove`` handlers will be present in the ``document.window`` object. Enabled by default if a touch device detected by the system and disabled otherwise. (Added in Qt 6.9) Note that some websites use this API to decide whether they run on a mobile device or on desktop and base their design on it. This can cause unwanted results on touchscreen laptops or other setups that emulate a fake touch device.
