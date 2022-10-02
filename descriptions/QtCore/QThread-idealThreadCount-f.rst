.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: ()
    :digest: 2b710933473bca0321b826e980f3b756

Returns the ideal number of threads that this process can run in parallel. This is done by querying the number of logical processors available to this process (if supported by this OS) or the total number of logical processors in the system. This function returns 1 if neither value could be determined.

**Note:** On operating systems that support setting a thread's affinity to a subset of all logical processors, the value returned by this function may change between threads and over time.

**Note:** On operating systems that support CPU hotplugging and hot-unplugging, the value returned by this function may also change over time (and note that CPUs can be turned on and off by software, without a physical, hardware change).
