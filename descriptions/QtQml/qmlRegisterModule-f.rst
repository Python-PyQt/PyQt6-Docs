.. sip:method-description::
    :status: todo
    :pysig: 40453122b44e8508ccafd2a3f0ffb95a
    :realsig: (const char*,int,int)
    :digest: dd13d2cc02a7a6529b0e2dd3652ce3df

This function registers a module in a particular *uri* with a version specified in *versionMajor* and *versionMinor*.

This can be used to make a certain module version available, even if no types are registered for that version. This is particularly useful for keeping the versions of related modules in sync.
