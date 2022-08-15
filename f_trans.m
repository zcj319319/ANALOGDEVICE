function out=f_trans(in,N_fft,fs,nq) % for dac nq=1 so no modification for now...
if mod(nq,2)
    out=in/N_fft*fs+(nq-1)/2*fs;
else
    out=nq/2*fs-in/N_fft*fs;
end