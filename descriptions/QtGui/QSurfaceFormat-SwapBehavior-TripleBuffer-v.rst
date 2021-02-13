.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: 974998fdeab60659f88b7cb832b05837

This swap behaviour is sometimes used in order to decrease the risk of skipping a frame when the rendering rate is just barely keeping up with the screen refresh rate. Depending on the platform it might also lead to slightly more efficient use of the GPU due to improved pipelining behaviour. Triple buffering comes at the cost of an extra frame of memory usage and latency, and might not be supported depending on the underlying platform.
