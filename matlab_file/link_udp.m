function u1=link_udp(ip,fs,fin,rbw,fstart,fstop)
    try
        fclose(instrfindall);
    catch
        warning('Address already in use');
    end
    u1=udp(ip,'RemotePort',1111,'LocalPort',1112);
%     u1=udp(ip,'RemotePort',1111,'LocalPort',1112);
    u1.DatagramReceivedFcn=@instrcallback;
    u1.ReadAsyncMode = 'continuous';
    % u1.BytesAvailableFcn = @BytesAvailable_Callback;
    u1.OutputBufferSize =4096;
    u1.InputBufferSize=4096;
    fopen(u1);
    if (~strcmp(u1.Status,'open'))
        NetworkError(u1,'Connection failed!');
    end
    fs_fin_rbw_start_stop=strp_1(fs,fin,rbw,fstart,fstop);
    fwrite(u1,fs_fin_rbw_start_stop);
end


function fs_fin_rbw_start_stop = strp_1(fs,fin,rbw,fstart,fstop)
    fs_fin_rbw_start_stop = zeros(1,45);
    fs_fin_rbw_start_stop(1)=hex2dec('aa');
    fs_fin_rbw_start_stop(2)=hex2dec('55');
    fs_fin_rbw_start_stop(3)=hex2dec('06');
    fs_fin_rbw_start_stop(4)=hex2dec('00');
    fs_fin_rbw_start_stop(5)=hex2dec('28');
    trans_hex_fs = num2hex(fs);
    for i=1:8
        fs_fin_rbw_start_stop(5+i)= hex2dec(trans_hex_fs(2*i-1:2*i));
    end
    trans_hex_fin = num2hex(fin);
    for i=1:8
        fs_fin_rbw_start_stop(13+i)= hex2dec(trans_hex_fin(2*i-1:2*i));
    end
    trans_hex_rbw = num2hex(rbw);
     for i=1:8
        fs_fin_rbw_start_stop(21+i)= hex2dec(trans_hex_rbw(2*i-1:2*i));
    end
    trans_hex_fstart = num2hex(fstart);
     for i=1:8
        fs_fin_rbw_start_stop(29+i)= hex2dec(trans_hex_fstart(2*i-1:2*i));
    end
    trans_hex_fstop = num2hex(fstop);
     for i=1:8
        fs_fin_rbw_start_stop(37+i)= hex2dec(trans_hex_fstop(2*i-1:2*i));
     end
end

function instrcallback(u1,evt) %#ok<INUSD>
    xback=fread(u1);
    data_list=xback(6:end);
    disp(num2str(evt.Data.AbsTime(6)));
    x_i_dec=typecast(uint8(data_list'),'double');
    fprintf("x_i_dec_1:%f\n",x_i_dec);
    assignin('base','x_i_dec',x_i_dec);
end


% function receive_data_prase(xback,count)
%     global sum_index,
%     global x;
%     global y;
%     global sum_logic;
%     if count ==8
%         if x==1
%             data_list=xback(6:end);
%             sum_index=typecast(uint8(data_list'),'double');
%             x=x+1;
%         end
%         if x==2
%             data_list=xback(6:end);
%             sum_logic=typecast(uint8(data_list'),'double');
%             x=1;
%         end
%     end
%     if count>8
%         if y==1
%             start_data_end_pre_1 = zeros(1,count/2);
%             start_data_end_stuffix_1 = zeros(1,count/2);
%             for i=1:count/16
%                 data_list=xback(6:6+count/2);
%                 data_str = data_list(8*i-7,8*i);
%                 start_data_end_pre_1(i)=typecast(uint8(data_str'),'double');
%             end
%             for i=1:count/16
%                 data_list=xback(6+count/2:end);
%                 data_str = data_list(8*i-7,8*i);
%                 start_data_end_stuffix_1(i)=typecast(uint8(data_str'),'double');
%             end
%             y=y+1;
%         end 
%         if y==2
%              start_data_end_pre_2 = zeros(1,count/2);
%              start_data_end_stuffix_2 = zeros(1,count/2);
%             for i=1:count/16
%                 data_list=xback(6:6+count/2);
%                 data_str = data_list(8*i-7,8*i);
%                 start_data_end_pre_2(i)=typecast(uint8(data_str'),'double');
%             end
%             for i=1:count/16
%                 data_list=xback(6+count/2:end);
%                 data_str = data_list(8*i-7,8*i);
%                 start_data_end_stuffix_2(i)=typecast(uint8(data_str'),'double');
%             end
%             y=y+1;
%         end
%         if y==3
%              start_data_end_pre_3 = zeros(1,count/2);
%              start_data_end_stuffix_3 = zeros(1,count/2);
%             for i=1:count/16
%                 data_list=xback(6:6+count/2);
%                 data_str = data_list(8*i-7,8*i);
%                 start_data_end_pre_3(i)=typecast(uint8(data_str'),'double');
%             end
%             for i=1:count/16
%                 data_list=xback(6+count/2:end);
%                 data_str = data_list(8*i-7,8*i);
%                 start_data_end_stuffix_3(i)=typecast(uint8(data_str'),'double');
%             end
%             y=1;
%         end
%     end
% end

function NetworkError(u1,msg)
    NetworkDispose(u1);
    error(msg);
end

function NetworkDispose(u1)  
    fclose(u1);
    delete(u1);
    clear u1;
    echoudp('off');
end


