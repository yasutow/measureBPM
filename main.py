import numpy as np
import time

if __name__=='__main__':
    idx=0
    lenary=30
    times=np.zeros(lenary)*np.nan
    bpms=np.zeros(lenary)*np.nan
    var = input("Push ENTER key to start")
    time_prev=time.time()
    while True:
        var = input("lap {0}".format(idx+1))
        time_now=time.time()
        times[idx%lenary]=time_now
        lap = (time_now-time_prev)
        bpm = 60.e0/lap
        bpms[idx%lenary]=bpm
        BPM=np.nanmean(bpms)
        print('{:.2f}'.format(BPM))
        time_prev=time_now
        idx=idx+1
