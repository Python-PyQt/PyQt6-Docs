.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: d85f0bee64a750c6e52ce0b5a7ca4ff2

Caching is enabled at the paint device level, in device coordinates. This mode is for items that can move, but are not rotated, scaled or sheared. If the item is transformed directly or indirectly, the cache will be regenerated automatically. Unlike ItemCoordinateCacheMode, DeviceCoordinateCache always renders at maximum quality.
