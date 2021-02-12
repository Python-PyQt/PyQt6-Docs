.. sip:method-description::
    :status: todo
    :pysig: d9a675468278ba0b4a48902f19589aa5
    :realsig: ()
    :digest: f65438e344d99473edc7b9432423656c

Returns the thread handle of the currently executing thread.

**Warning:** The handle returned by this function is used for internal purposes and should not be used in any application code.

**Note:** On Windows, this function returns the DWORD (Windows-Thread ID) returned by the Win32 function GetCurrentThreadId(), not the pseudo-HANDLE (Windows-Thread HANDLE) returned by the Win32 function GetCurrentThread().
