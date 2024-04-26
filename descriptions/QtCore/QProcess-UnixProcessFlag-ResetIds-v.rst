.. sip:enum-member-description::
    :status: todo
    :value: 0x0100
    :digest: 95dd1e4f803dbcd47d3068269c5e8c57

Drops any retained, effective user or group ID the current process may still have (see ``setuid(2)`` and ``setgid(2)``, plus QCoreApplication::setSetuidAllowed()). This is useful if the current process was setuid or setgid and does not wish the child process to retain the elevated privileges.
