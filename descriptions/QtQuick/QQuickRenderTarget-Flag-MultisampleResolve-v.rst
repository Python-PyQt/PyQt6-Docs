.. sip:enum-member-description::
    :status: todo
    :value: 0x01
    :digest: e6bddeb24862aa62758be2204d1e4a36

Indicates that the ``sampleCount`` argument is not the number of samples for the provided texture (and that the texture is still a non-multisample texture), but rather the desired samples for multisample antialiasing. Triggers automatically creating and managing an intermediate multisample texture (or texture array) as the color buffer, transparently to the application. The samples are resolved into the provided texture at the end of the render pass automatically. When this flag is not set, and the ``sampleCount`` argument is greater than 1, it implies the provided texture is multisample. The flag has no effect is the ``sampleCount`` is 1 (indicating that multisampling is not involved).
