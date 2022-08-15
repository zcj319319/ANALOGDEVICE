close all;
% clear all;
%data = textread('D:\projects\DIQUN\TR9xxx_v5\TR9xxx\memory_dump_data.txt', '%s');
data = textread('memory_dump_data.txt', '%s');
% data = textread('memory_dump_rd.txt', '%s');
data = hex2dec(data);

smpBitsMode = 256;
sectNum = 16;
sectBits = 32;
wordBits = 8;
sectWords = sectBits/wordBits;
memoryVol = 2^16;
smpVol = memoryVol*wordBits/smpBitsMode;
smpWords = smpBitsMode/wordBits;

nodeSectVol = sectNum*sectBits/smpBitsMode;

sectMemoryVol = memoryVol/sectNum/sectWords;

dataStructMap = zeros(sectNum, sectMemoryVol, sectWords);

%id=fopen('dataIdx.txt','w');

for sectIdx=1:sectNum
    for sectVolIdx=1:sectMemoryVol
        for sectWordIdx=1:sectWords
            dataIdx=(sectIdx - 1)*sectMemoryVol*sectWords + (sectVolIdx - 1)*sectWords + sectWordIdx;
%             fprintf('sectIdx=%10d, sectVolIdx=%10d, sectWordIdx=%10d, dataIdx=%10d\n',sectIdx, sectVolIdx, sectWordIdx, dataIdx);
            dataStructMap(sectIdx, sectVolIdx, sectWordIdx) = data(dataIdx);
        end
    end
end

%fclose(id);

smpData=zeros(smpVol, smpWords);

%id2=fopen('sectIdx.txt','w');

for smpVolIdx=1:smpVol
    if smpVolIdx>1024
        addNum=8;
    else
        addNum=0;
    end
    for smpWordIdx=1:smpWords
        sectIdx=floor((smpWordIdx-1)/sectWords) + 1+addNum;
        sectVolIdx=mod(smpVolIdx - 1,sectMemoryVol)+1;
        sectWordIdx=mod(smpWordIdx - 1, sectWords)+1;
       
%         fprintf('sectIdx=%10d, sectVolIdx=%10d, sectWordIdx=%10d\n',sectIdx, sectVolIdx, sectWordIdx);
        smpData(smpVolIdx, smpWordIdx)=dataStructMap(sectIdx,sectVolIdx,sectWordIdx);
    end
end

%fclose(id2);
data_out_i=smpData(:,1:16);  %I data
data_out_q=smpData(:,17:32);  %Q data
%data_out_q=smpData(:,1:16);
data_out_i_full = zeros(1,4096*4);
for comb = 1:2048
    for i = 1:8
        temp_l = data_out_i(comb,2*i-1);
        temp_h = data_out_i(comb,2*i);
        hex_full = temp_h*2^8 + temp_l;
        if ( hex_full>=2^15 )
              data_out_i_full(comb*8+i-8) = hex_full -2^16;
        else
              data_out_i_full(comb*8+i-8) = hex_full;
        end
    end
end
data_out_q_full = zeros(1,4096*4);
for comb = 1:4096/2
    for i = 1:8
        temp_l = data_out_q(comb,2*i-1);
        temp_h = data_out_q(comb,2*i);
        hex_full = temp_h*2^8 + temp_l;
        if ( hex_full>=2^15 )
              data_out_q_full(comb*8+i-8) = hex_full -2^16;
        else
              data_out_q_full(comb*8+i-8) = hex_full;
        end
    end
end
data_out_i_full_Ext = data_out_i_full;
% data_out_i_full = data_out_i_full_Ext(5:16384+4);
% data_temp=[data_out_i_full(5:8:end); ...
%     data_out_i_full(6:8:end); ...
%     data_out_i_full(7:8:end); ...
%     data_out_i_full(8:8:end); ...
%     data_out_i_full(1:8:end); ...
%     data_out_i_full(2:8:end); ...
%     data_out_i_full(3:8:end); ...
%     data_out_i_full(4:8:end)];

% data_temp=[data_out_i_full(4:8:end); ...
%     data_out_i_full(3:8:end); ...
%      data_out_i_full(2:8:end); ...
%      data_out_i_full(1:8:end)];
% 
data_temp=data_out_q_full(1:1:length(data_out_i_full));

% data = data_temp;
% rx_corr.man_stdAB=std(data(1:4:end))/std(data(2:4:end));
% rx_corr.man_stdAC=std(data(1:4:end))/std(data(3:4:end));
% rx_corr.man_stdAD=std(data(1:4:end))/std(data(4:4:end));
% rx_corr.man_corrAC=sum(data(1:4:end-4).*data(3:4:end-4)-data(3:4:end-4).*data(5:4:end));
% rx_corr.man_corrABC=sum(data(1:4:end).*data(2:4:end)*rx_corr.man_stdAB-data(2:4:end).*data(3:4:end)*rx_corr.man_stdAC);
% rx_corr.man_corrCDA=sum(data(3:4:end-4).*data(4:4:end-4)*rx_corr.man_stdAC*rx_corr.man_stdAD-data(4:4:end-4).*data(5:4:end)*rx_corr.man_stdAD);
% rx_corr
% %data_temp=data_out_i_full(1:1:end)+1*j*data_out_q_full(1:1:end);
% plot(data_temp(1:1:end),'b');
% figure()
% plot(data_out_i_full(1:4:end),'y'); 
% figure;
% plot(data_out_i_full(1:8:end),'y'); 
% xtemp=data_out_i_full(1:8:end);
% plot(xtemp(1:3:end));hold on;
% plot(xtemp(2:3:end));
% plot(xtemp(3:3:end));
% xtemp2=data_out_i_full(2:8:end); 
% plot(xtemp2(1:3:end));hold on;
% plot(xtemp2(2:3:end));
% plot(xtemp2(3:3:end));
% xtemp3=data_out_i_full(3:8:end); 
% plot(xtemp3(1:3:end));hold on;
% plot(xtemp3(2:3:end));
% plot(xtemp3(3:3:end));
% 
% 
% plot(data_temp(3:1:100),'c');  
% hold on;
% plot(data_temp(4:2:100),'k');  
% hold on;
% plot(data_temp(1:8:end),'r');  
% hold on;
% plot(data_temp(6:8:end),'g');  
% hold on;
% plot(data_temp(4:8:end),'b');  
% hold on;
% plot(data_temp(2:8:end),'r');  
% 
%  
% data_i_fft =data_out_i_full(1:24:end);
% data_fft = 20*log10(abs(fft(data_i_fft)));
% figure;
% plot(data_temp);

dcm=1;
fs = 3e9/dcm;
% para.sigbw=100e6;
% para.dpdbw=300e6;
para.sideband=3000;
para.sideband_sig=10e6;
para.fullscale=1200;
para.Rl=100;
para.num_interleave=4;
para.num_HD=5;
para.window='hann';
para.nyquitst_zone=2;
para.dacOSR=1;
% para.imd_mode=1;
para.plot_range=0;
para.simple_plot=0;
para.dc_1f_noise_cancel=20e6;      %% add cancel dc  and 1/f noise
para.dbc_th_HD=-20;                %% not add color for -70dbc
para.dbc_th_IMD=-20;
para.dbc_th_IL=-20;    
para.dbc_th_SFDR=-20;
perf=fft_calc_tot(data_temp,fs,15,2,para);
% perf=fft_calc(data_temp(4:4:end),fs/4,15,para);
% return
% gain2=std(data_temp(1:4:end))/std(data_temp(2:4:end));
% gain3=std(data_temp(1:4:end))/std(data_temp(3:4:end));
% gain4=std(data_temp(1:4:end))/std(data_temp(4:4:end));
% 
% data_temp2=data_temp;
% data_temp2(2:4:end)=data_temp2(2:4:end)*gain2;
% data_temp2(3:4:end)=data_temp2(3:4:end)*gain3;
% data_temp2(4:4:end)=data_temp2(4:4:end)*gain4;
% perf=fft_calc_tot(data_temp2,fs,15,2,para);
% 
% fin=450e6;
% corrAC=mean(data_temp(1:4:end-4).*data_temp(3:4:end-4)-data_temp(3:4:end-4).*data_temp(5:4:end));
% corrB=mean(data_temp(1:4:end-4).*data_temp(2:4:end-4)-data_temp(2:4:end-4).*data_temp(3:4:end-4));
% corrD=mean(data_temp(3:4:end-4).*data_temp(4:4:end-4)-data_temp(4:4:end-4).*data_temp(5:4:end));
% skewAC=corrAC/std(data_temp(1:4:end-4))^2/2/pi/fin/sin(2*pi*2*fin/fs);
% skewB=corrB/std(data_temp(1:4:end-4))^2/2/pi/fin/sin(2*pi*fin/fs);
% skewD=corrD/std(data_temp(1:4:end-4))^2/2/pi/fin/sin(2*pi*fin/fs);
% gain234=[gain2 gain3 gain4]
% corr=[corrAC corrB corrD]
% skew=[skewAC skewB skewD]*1e15
% b=smpData(:,17:32);
