.. sip:enum-member-description::
    :status: todo
    :value: 130
    :digest: e4a8e7c78df9f95e24c40c844352fe2e

A QWidget respects the safe area margins of a window by incorporating the margins into its contents' margins by default. This means, that a QLayout will use the content area of a widget for its layout, unless the  attribute is set. This along with a contents margin of 0 can be used on the actual layout, to allow for example a background image to underlay the status bar and other system areas on an iOS device, while still allowing child widgets of that background to be inset based on the safe area.
