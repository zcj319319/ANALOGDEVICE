function []=send_db_content(ip,start_db,midle_index_1,midle_index_2,end_db,threshold_value_1,threshold_value_2,threshold_value_3,bw_1,bw_2,bw_3,holder)
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
    encapsulation_data=ustrp(start_db,midle_index_1,midle_index_2,end_db,threshold_value_1,threshold_value_2,threshold_value_3,bw_1,bw_2,bw_3,holder);
    fwrite(u1,encapsulation_data);
end

function encapsulation_data = ustrp(start_db,midle_index_1,midle_index_2,end_db,threshold_value_1,threshold_value_2,threshold_value_3,bw_1,bw_2,bw_3,holder)
    encapsulation_data = zeros(1,93);
    encapsulation_data(1)=hex2dec('aa');
    encapsulation_data(2)=hex2dec('55');
    encapsulation_data(3)=hex2dec('06');
    encapsulation_data(4)=hex2dec('00');
    encapsulation_data(5)=hex2dec('50');
    trans_hex_start_db = num2hex(start_db);
    for i=1:8
        encapsulation_data(5+i)= hex2dec(trans_hex_start_db(2*i-1:2*i));
    end
    trans_hex_midle_index_1 = num2hex(midle_index_1);
    for i=1:8
        encapsulation_data(13+i)= hex2dec(trans_hex_midle_index_1(2*i-1:2*i));
    end
    trans_hex_midle_index_2 = num2hex(midle_index_2);
     for i=1:8
        encapsulation_data(21+i)= hex2dec(trans_hex_midle_index_2(2*i-1:2*i));
    end
    trans_hex_fend_db = num2hex(end_db);
     for i=1:8
        encapsulation_data(29+i)= hex2dec(trans_hex_fend_db(2*i-1:2*i));
    end
    trans_hex_threshold_value_1 = num2hex(threshold_value_1);
     for i=1:8
        encapsulation_data(37+i)= hex2dec(trans_hex_threshold_value_1(2*i-1:2*i));
     end
     trans_hex_threshold_value_2 = num2hex(threshold_value_2);
     for i=1:8
        encapsulation_data(45+i)= hex2dec(trans_hex_threshold_value_2(2*i-1:2*i));
     end
      trans_hex_threshold_value_3 = num2hex(threshold_value_3);
     for i=1:8
        encapsulation_data(53+i)= hex2dec(trans_hex_threshold_value_3(2*i-1:2*i));
     end
     trans_hex_threshold_bw_1 = num2hex(bw_1);
     for i=1:8
        encapsulation_data(61+i)= hex2dec(trans_hex_threshold_bw_1(2*i-1:2*i));
     end
     trans_hex_threshold_bw_2 = num2hex(bw_2);
     for i=1:8
        encapsulation_data(69+i)= hex2dec(trans_hex_threshold_bw_2(2*i-1:2*i));
     end
     trans_hex_threshold_bw_3 = num2hex(bw_3);
     for i=1:8
        encapsulation_data(77+i)= hex2dec(trans_hex_threshold_bw_3(2*i-1:2*i));
     end
     trans_hex_holder = num2hex(holder);
     for i=1:8
        encapsulation_data(85+i)= hex2dec(trans_hex_holder(2*i-1:2*i));
     end
end

function instrcallback(u1,evt) %#ok<INUSD>
    global x_i_dec;
    xback=fread(u1);
    flag=xback(3);
    count_msb = xback(4);
    count_lsb = xback(5);
    count = count_lsb+count_msb*256;
    switch(flag)
        case 6
            xback=fread(u1);
            data_list=xback(6:end);
            x_i_dec=typecast(uint8(data_list'),'double');
            fprintf("%f\n",x_i_dec);
        case 7
            receive_data_prase(xback,count);
    end
end


function receive_data_prase(xback,count)
    global sum_index
    if count ==8
        data_list=xback(6:end);
        sum_index=typecast(uint8(data_list'),'double');
    end
    if count>8
        start_data_end_pre_1 = zeros(1,count/2);
        start_data_end_stuffix_1 = zeros(1,count/2);
        for i=1:count/16
            data_list=xback(6:6+count/2);
            data_str = data_list(8*i-7,8*i);
            start_data_end_pre_1(i)=typecast(uint8(data_str'),'double');
        end
        for i=1:count/16
            data_list=xback(6+count/2:end);
            data_str = data_list(8*i-7,8*i);
            start_data_end_stuffix_1(i)=typecast(uint8(data_str'),'double');
        end
    end
end

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
