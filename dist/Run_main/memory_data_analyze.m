function [perf] = memory_data_analyze(path,config,para)
    data = textread(path, '%s');
    data = hex2dec(data);
	sample_rate = config.sample_rate;
    smpBitsMode = config.smpBitsMode;
    sectNum = config.sectNum;
    sectBits = config.sectBits;
    wordBits = config.wordBits;
    memoryVol = config.memoryVol;
    sectWords = sectBits/wordBits;
    smpVol = memoryVol*wordBits/smpBitsMode;
    smpWords = smpBitsMode/wordBits;
%     nodeSectVol = sectNum*sectBits/smpBitsMode;
    sectMemoryVol = memoryVol/sectNum/sectWords;
    dataStructMap = zeros(sectNum, sectMemoryVol, sectWords);
    %数据转换为map     
    for sectIdx=1:sectNum
    for sectVolIdx=1:sectMemoryVol
        for sectWordIdx=1:sectWords
            dataIdx=(sectIdx - 1)*sectMemoryVol*sectWords + (sectVolIdx - 1)*sectWords + sectWordIdx;
%             fprintf('sectIdx=%10d, sectVolIdx=%10d, sectWordIdx=%10d, dataIdx=%10d\n',sectIdx, sectVolIdx, sectWordIdx, dataIdx);
            dataStructMap(sectIdx, sectVolIdx, sectWordIdx) = data(dataIdx);
        end
    end
    end
    % 采样数据
    smpData=zeros(smpVol, smpWords);
    for smpVolIdx=1:smpVol
    if smpVolIdx>1024
        addNum=8;
    else
        addNum=0;
    end
    for smpWordIdx=1:smpWords
        sectIdx=floor((smpWordIdx-1)/sectWords) + 1+addNum;
		%fprintf('sectIdx=%d,smpVolIdx=%d\n',sectIdx,smpVolIdx);
        sectVolIdx=mod(smpVolIdx - 1,sectMemoryVol)+1;
        sectWordIdx=mod(smpWordIdx - 1, sectWords)+1;
        %fprintf('sectIdx=%d,smpVolIdx=%d\n',sectIdx,smpVolIdx);
		%fprintf('sectIdx=%10d, sectVolIdx=%10d, sectWordIdx=%10d\n',sectIdx, sectVolIdx, sectWordIdx);
        smpData(smpVolIdx, smpWordIdx)=dataStructMap(sectIdx,sectVolIdx,sectWordIdx);
    end
    end
    
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %
    data_out_i=smpData(:,1:smpWords/2);  %I data
    data_out_q=smpData(:,smpWords/2+1:smpWords);  %Q data
    data_out_i_full = zeros(1,length(smpData)*8);
    for comb = 1:length(smpData)
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
    data_out_q_full = zeros(1,length(smpData)*8);
    for comb = 1:length(smpData)
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
    data_temp=data_out_q_full(1:1:length(data_out_i_full));
    dcm=1;
    fs = sample_rate/dcm;
    perf=fft_calc_tot(data_temp,fs,2,1,para);
end

