close all; clear; clc;

% Setting 204b link parameters
l = 8; m = 2; f = 2; n_pie = 16;
%     l = 1 ;m = 1; f = 2 ;n_pie = 16;
fsx4_en=0;
%   l = 8;  m = 8; f = 4;n_pie = 16;


% % Setting spectrum analysis parameters
% dcm = 1;
% fs = 2200e6/dcm;
% para.sideband=300;
%
% para.sideband_sig=3e6;
% para.fullscale=1200;
% para.Rl=100;
% para.num_interleave=4;
% para.num_HD=7;
% para.window='hann';
% para.nyquitst_zone=1;
% para.dacOSR=1;
% para.plot_range=0;
% para.simple_plot=0;
% para.dc_1f_noise_cancel=20e6;      %% add cancel dc  and 1/f noise
% para.dbc_th_HD=-20;                %% not add color for -70dbc
% para.dbc_th_IMD=-20;
% para.dbc_th_IL=-20;
% para.dbc_th_SFDR=-20;
% freq=[0.255e9,0.765e9,0.9e9,1.8e9,2.1e9,2.6e9,3.95e9,4.9e9,5.9e9];
freq=[2.6e9,1.8445e9,2.655e9];
% freq=[5.9e9];
% set board test para
board='single_TEM+30_num8_cha_';
% 0x311-0x1--channalb
% 0x311-0x4--channala
corner = 'tt';
amp_set=[-8,-15];

chipid=0;
writefile=1;
freq_cw=freq(1);
IMD_mode=1;
freq_cwl=freq_cw-0.0025e9;
freq_cwr=freq_cw+0.0025e9;

% Instantiate FPGA Data Capture System object
if ~exist('diqun_jtag','var') || ~isa(diqun_jtag,'f2m') || ~isprop(diqun_jtag,'TimeStamp') || ~strcmpi(diqun_jtag.TimeStamp,'17-May-2021 11:05:08')
    diqun_jtag = f2m;
end

for i_freq=1:size(freq,2)
    freq_cw=freq(i_freq);
    for iamp=1:length(amp_set)
        idea_amp1=amp_set(iamp);
        amp=5;                                %set amp to instrument
        loss=0;                                %set loss to instrument
        if IMD_mode
            Control_SG_sig1(freq_cwl,amp,loss);      %set instrument
            Control_SG_sig2(freq_cwr,amp,loss);
        else
            Control_SG_sig1(freq_cw,amp,loss);
        end
        i_loop=0;
        while (i_loop<5)
            [~,sysref,valid,d0,d1,d2,d3,d4,d5,d6,d7,sof]=step(diqun_jtag);
            link_data = [double([d0,d1,d2,d3,d4,d5,d6,d7]), double(sof)]';
            converter_data = [transport(link_data, l, f, m, n_pie,fsx4_en)]';
            
            adc_data = converter_data(:,1);
            
            pause(2);
            
            fs = 3.0e9;
            
            para.sideband=300;
            para.sideband_sig=3e6;
            para.fullscale=1200;
            para.Rl=100;
            para.num_interleave=4;
            para.num_HD=4;
            
            para.num_IMD=3;
            para.imd_mode=1;
            
            para.window='hann';
            para.nyquitst_zone=floor(freq_cw/(fs/2))+1;
            para.dacOSR=1;
            para.plot_range=0;
            para.simple_plot=0;
            para.dc_1f_noise_cancel=20e6;      %% add cancel dc  and 1/f noise
            para.dbc_th_HD=-70;                %% not add color for -70dbc
            para.dbc_th_IMD=-70;
            para.dbc_th_IL=-70;
            para.dbc_th_SFDR=-70;
            para.figure_overwrite=1;
            if IMD_mode
                str_file=strcat(date,'_',num2str(freq_cw,'%2.3E'),'_',board,num2str(idea_amp1),'_','Double_tune_');
            else
                str_file=strcat(date,'_',num2str(freq_cw,'%2.3E'),'_',board,num2str(idea_amp1),'_');
            end
            if chipid==0
                % test for diqun0 channela
                perf0a=fft_calc_tot(converter_data(1:65536,1),fs,15,1,para);
                if abs(perf0a.SIG1_dbfs-idea_amp1)>0.2
                    amp_delta=idea_amp1-perf0a.SIG1_dbfs;
                    amp=amp+amp_delta;
                end
                if amp>20
                    amp=19;
                end
                if IMD_mode
                    Control_SG_sig1(freq_cwl,amp,loss);      %set instrument
                    Control_SG_sig2(freq_cwr,amp,loss);
                else
                    Control_SG_sig1(freq_cw,amp,loss);
                end
                pause(1);
                perf0a_t=struct2table(perf0a,'AsArray',true);
                if writefile
                    if IMD_mode
                        writetable(perf0a_t,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\spec\',strcat(date,'_',board,num2str(idea_amp1),'_',num2str(fs,'%2.3E'),'Double_tune','_my_spec.xls')),'Sheet',1,"WriteMode","append");
                        save(strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\',str_file,'my_data_0a.mat'), 'converter_data', 'perf0a');
                        fig1=figure(1);
                        set(fig1,'outerposition',get(0,'screensize'));
                        exportgraphics(fig1,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\picture\',str_file,'_',board,num2str(i_loop),'_',num2str(fs,'%2.3E'),'diqun0a.jpg'),'Resolution',200);
                    else
                        writetable(perf0a_t,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\spec\',strcat(date,'_',board,num2str(idea_amp1),'_',num2str(fs,'%2.3E'),'_my_spec.xls')),'Sheet',1,"WriteMode","append");
                        save(strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\data\',str_file,'my_data_0a.mat'), 'converter_data', 'perf0a');
                        fig1=figure(1);
                        set(fig1,'outerposition',get(0,'screensize'));
                        exportgraphics(fig1,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\picture\',str_file,'_',board,num2str(i_loop),'_',num2str(fs,'%2.3E'),'diqun0a.jpg'),'Resolution',200);
                        
                    end
                end
            end
            if chipid==1
                %test for diqun0 channelb
                perf0b=fft_calc_tot(converter_data(1:65536,2),fs,15,2,para);
                if abs(perf0b.SIG1_dbfs-idea_amp1)>0.2
                    amp_delta=idea_amp1-perf0b.SIG1_dbfs;
                    amp=amp+amp_delta;
                end
                if amp>20
                    amp=19;
                end
                Control_SG_sig1(freq_cw,amp,loss);
                pause(1);
                perf0b_t=struct2table(perf0b,'AsArray',true);
                if writefile
                    if IMD_mode
                        writetable(perf0b_t,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\spec\',strcat(date,'_',board,num2str(idea_amp1),'_',num2str(fs,'%2.3E'),'Double_tune','_my_spec.xls')),'Sheet',2,"WriteMode","append");
                        save(strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\data\',str_file,'my_data_0a.mat'), 'converter_data', 'perf0b');
                        fig2=figure(2);
                        set(fig2,'outerposition',get(0,'screensize'));
                        exportgraphics(fig2,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\picture\',str_file,'_',board,num2str(i_loop),'_',num2str(fs,'%2.3E'),'diqun0b.jpg'),'Resolution',200);
                    else
                        writetable(perf0b_t,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\spec\',strcat(date,'_',board,num2str(idea_amp1),'_',num2str(fs,'%2.3E'),'_my_spec.xls')),'Sheet',2,"WriteMode","append");
                        save(strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\data\',str_file,'my_data_0b.mat'), 'converter_data', 'perf0b');
                        fig2=figure(2);
                        set(fig2,'outerposition',get(0,'screensize'));
                        exportgraphics(fig2,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\picture\',str_file,'_',board,num2str(i_loop),'_',num2str(fs,'%2.3E'),'diqun0b.jpg'),'Resolution',200);
                    end
                end
                
            end
            % test for diqun0 channela
            drawnow;
            pause(1);
            i_loop=i_loop+1;
        end
    end
    %     if writefile
    %         if chipid==0
    %             fig1=figure(1);
    %             set(fig1,'outerposition',get(0,'screensize'));
    %             exportgraphics(fig1,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\picture\',str_file,'diqun0a.jpg'),'Resolution',200);
    %             %             fig2=figure(2);
    %             %             set(fig2,'outerposition',get(0,'screensize'));
    %             %             exportgraphics(fig2,strcat('D:\dual_diqun_2022\dual_diqun_2022\matlab\sample_test\data\picture\',str_file,'diqun0b.jpg'),'Resolution',200);
    %         end
    %     end
    pause(5);
end
release(diqun_jtag);