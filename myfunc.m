function [index x] = myfunc()
    index=[];
    x=[];
    for i = 1:255
        index=[index i];
        x=[x exp(-i/150.0)*cos(i/10.0)];
    end
end

