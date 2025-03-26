import numpy as np
import os

import matplotlib
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# matplotlib.use('tkagg')
#matplotlib.use('Qtagg')
import matplotlib.pyplot as plt

def show_iq_one_channel(filenmae_1, shift, length):
    sample_rate = 28e6  # 28 MS/s
    center_freq = 2.4e9  # 2.4 GHz

    title_1 = f'[I] Channel 0 Waveform (f_c = {center_freq/1e9} GHz, f_s = {sample_rate/1e6} MHz)';
    title_2 = f'[Q] Channel 0 Waveform (f_c = {center_freq/1e9} GHz, f_s = {sample_rate/1e6} MHz)';

    if not os.path.exists(filenmae_1):
        raise FileNotFoundError(f"檔案 {filenmae_1} 不存在")

    data_1 = np.fromfile(filenmae_1, dtype=np.complex64)
    num_samples = len(data_1)

    # 創建時間軸
    time = np.arange(num_samples) / sample_rate

    fig, ax = plt.subplots(2, 1, figsize=(8, 6))  # ax 是陣列 [ax[0], ax[1]]
    text_1 = ax[0].text(0.02, 0.85, '', transform=ax[0].transAxes, fontsize=14, color='red')
   
    stop = shift + length
    is_real = True
    draw_signal(time[shift:stop], data_1[shift:stop], is_real, ax[0], 'I (Real)', title_1)
    draw_signal(time[shift:stop], data_1[shift:stop], not is_real, ax[1], 'Q (Imag)', title_2)
 
    def on_click(event):
        strxy = 'no data'
        if event.inaxes == ax[0]:
            x_data = event.xdata
            y_data = event.ydata
            strxy = f'channel 0: x={x_data:.7f}, y={y_data}'
            text_1.set_text(strxy)
        print(strxy)
        fig.canvas.draw_idle()  # 刷新畫面

    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.tight_layout()
    plt.show()

    print(f"總樣本數: {len(data_1)}")
    print(f"每個通道的樣本數: {num_samples}")
    print(f"總時長: {num_samples/sample_rate*1e3:.2f} ms")

def show_iq_two_channels(filename_prefix, shift, length):
    sample_rate = 28e6  # 28 MS/s
    center_freq = 2.4e9  # 2.4 GHz

    filenmae_1 = filename_prefix + ".0.dat"  # filename_prefix = iq_f2.4_bw20m_g0_d3m_S45
    filenmae_2 = filename_prefix + ".1.dat"

    title_1 = f'Channel 0 Waveform (f_c = {center_freq/1e9} GHz, f_s = {sample_rate/1e6} MHz)';
    title_2 = f'Channel 1 Waveform (f_c = {center_freq/1e9} GHz, f_s = {sample_rate/1e6} MHz)';

    if not os.path.exists(filenmae_1):
        raise FileNotFoundError(f"檔案 {filenmae_1} 不存在")
    if not os.path.exists(filenmae_2):
        raise FileNotFoundError(f"檔案 {filenmae_2} 不存在")

    data_1 = np.fromfile(filenmae_1, dtype=np.complex64)
    data_2 = np.fromfile(filenmae_2, dtype=np.complex64)

    num_samples = len(data_1)

    # 創建時間軸
    time = np.arange(num_samples) / sample_rate

    fig, ax = plt.subplots(2, 1, figsize=(8, 6))  # ax 是陣列 [ax[0], ax[1]]
    text_1 = ax[0].text(0.02, 0.85, '', transform=ax[0].transAxes, fontsize=14, color='red')
    text_2 = ax[1].text(0.02, 0.85, '', transform=ax[1].transAxes, fontsize=14, color='blue')
   
    stop = shift + length
    is_real = True;
    draw_signal(time[shift:stop], data_1[shift:stop], is_real, ax[0], 'I (Real)', title_1)
    draw_signal(time[shift:stop], data_2[shift:stop], is_real, ax[1], 'I (Real)', title_2)
 
    def on_move(event):
        strxy = 'no data'
        if event.inaxes == ax[0]:
            x_data = event.xdata
            y_data = event.ydata
            strxy = f'channel 0: x={x_data}, y={y_data:.2f}'
            text_1.set_text(strxy)
            #text_2.set_text(strxy)
        elif event.inaxes == ax[1]:
            x_data = event.xdata
            y_data = event.ydata
            strxy = f'channel 1: x={x_data}, y={y_data:.2f}'
            text_2.set_text(strxy)
            #text_1.set_text('')
        print(strxy)
        fig.canvas.draw_idle()  # 刷新畫面

    def on_click(event):
        strxy = 'no data'
        if event.inaxes == ax[0]:
            x_data = event.xdata
            y_data = event.ydata
            strxy = f'channel 0: x={x_data:.7f}, y={y_data}'
            text_1.set_text(strxy)
        elif event.inaxes == ax[1]:
            x_data = event.xdata
            y_data = event.ydata
            strxy = f'channel 1: x={x_data:.7f}, y={y_data}'
            text_2.set_text(strxy)
        print(strxy)
        fig.canvas.draw_idle()  # 刷新畫面

    # fig.canvas.mpl_connect('motion_notify_event', on_move)  
    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.tight_layout()
    plt.show()

    print(f"總樣本數: {len(data_1)}")
    print(f"每個通道的樣本數: {num_samples}")
    print(f"總時長: {num_samples/sample_rate*1e3:.2f} ms")

def draw_signal(time, data, is_real, ax, label, title):
    if is_real:
        ax.plot(time, np.real(data), label=label)
    else:
        ax.plot(time, np.imag(data), label=label)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)