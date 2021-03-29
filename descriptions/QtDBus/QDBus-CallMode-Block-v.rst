.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 9ef21007ea7fcdfd092d452ecd8e6ad6

Don't use an event loop to wait for a reply, but instead block on network operations while waiting. This means the user-interface may not be updated until the function returns.
