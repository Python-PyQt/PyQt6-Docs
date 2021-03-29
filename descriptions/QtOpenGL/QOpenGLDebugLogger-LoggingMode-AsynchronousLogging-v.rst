.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: d965752d7cf8524ef6959e519c0f6ae1

Messages from the OpenGL server are logged asynchronously. This means that messages can be logged some time after the corresponding OpenGL actions that caused them, and even be received in an out-of-order fashion, depending on the OpenGL implementation. This mode has a very low performance penalty, as OpenGL implementations are heavily threaded and asynchronous by nature.
