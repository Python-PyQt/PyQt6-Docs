.. sip:enum-member-description::
    :status: todo
    :value: 0x08
    :realname: QLibrary::LoadHint::PreventUnloadHint
    :digest: 6a9ae65d5c366740a54a03339f732d2f

Prevents the library from being unloaded from the address space if close() is called. The library's static variables are not reinitialized if open() is called at a later time.
