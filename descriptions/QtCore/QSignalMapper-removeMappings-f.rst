.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: 07a8c739ba351b077daed7312718e99f

Removes all mappings for *sender*.

This is done automatically when mapped objects are destroyed.

**Note:** This does not disconnect any signals. If *sender* is not destroyed then this will need to be done explicitly if required.
