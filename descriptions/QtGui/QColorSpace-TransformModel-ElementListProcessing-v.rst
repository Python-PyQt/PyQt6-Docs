.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 0650edb737dcacf2c7c8c6a2d5d9c6dc

The transforms are one or two lists of processing elements that can do many things, each list only process either to the connection color space or from it. This is very flexible, but rather slow, and can only be set by reading ICC profiles (See :sip:ref:`~PyQt6.QtGui.QColorSpace.fromIccProfile`). Since the two lists are separate a color space on this form can be a valid source, but not necessarily also a valid target. When changing either primaries or transfer function on a color space on this type it will reset to an empty ThreeComponentMatrix form.
