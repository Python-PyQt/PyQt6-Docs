.. sip:enum-member-description::
    :status: todo
    :value: 0x1
    :digest: e6af6113c2f805d79a0a267709d41bc4

Indicates that the URL scheme is `potentially trustworthy <https://www.w3.org/TR/powerful-features/#is-origin-trustworthy>`_. This flag should only be applied to URL schemes which ensure data authenticity, confidentiality, and integrity, either through encryption or other means. Examples of secure builtin schemes include ``https`` (authenticated and encrypted) and ``qrc`` (local resources only), whereas ``http`` is an example of an insecure scheme.
