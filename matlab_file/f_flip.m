function out=f_flip(in,nq)
if mod(nq,2)
    out=in;
else
    out=fliplr(in);
end