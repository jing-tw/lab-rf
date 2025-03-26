import numpy as np
import argparse
import os
import matplotlib.pyplot as plt
import matplotlib



def show(filename, length):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"檔案 {filename} 不存在")
        
    sample_rate = 28e6  # 28 MS/s
    center_freq = 2.4e9  # 2.4 GHz

    data = np.fromfile(filename, dtype=np.complex64)
    num_samples = len(data)

    # 創建時間軸
    time = np.arange(num_samples) / sample_rate

    # 通道 0
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))  # ax 是陣列 [ax[0], ax[1]]
    text = ax[0].text(0.02, 0.95, '', transform=ax[0].transAxes)
   
    panelIndex = 0
    drawSignal(time[:length], data[:length], ax[panelIndex], label='I (Real)')
    plt.grid(True)
    plt.tight_layout()
    plt.title(f'Channel 0 Waveform (f_c = {center_freq/1e9} GHz, f_s = {sample_rate/1e6} MHz)')
    plt.show()

    print(f"總樣本數: {len(data)}")
    print(f"每個通道的樣本數: {num_samples}")
    print(f"總時長: {num_samples/sample_rate*1e3:.2f} ms")
 
    def on_move(event):
        if event.inaxes != ax:
            return
        x_data = event.xdata
        y_data = event.ydata
        text.set_text(f'x={x_data:.2f}, y={y_data:.2f}')
        plt.draw()

    fig.canvas.mpl_connect('motion_notify_event', on_move)

def drawSignal(time, data, ax, label):
    ax.plot(time, np.real(data), label=label)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.legend()

def main():
    # 設置命令列參數解析
    parser = argparse.ArgumentParser(description="繪製 I/Q 數據波形")
    parser.add_argument("filename", type=str, help="輸入的 .dat 檔案路徑")
    args = parser.parse_args()

    #filename = "./20250225/iq_f2.4_bw20m_g0_d3m_S45.0.dat"
    show(args.filename, 10000)

# Usage:
# python show-iq.py ./20250225/iq_f2.4_bw20m_g0_d3m_S45.0.dat
# python show-iq.py "D:\work\project\20.06.4-CUAS-Passive radar phase I\receiver\data\20250225\iq_f2.4_bw20m_g0_d3m_S45.0.dat"
# python show-iq-show-one-wave.py "D:\work\project\20.06.4-CUAS-Passive radar phase I\receiver\data\20250325\b210_freq2.4g_bw50m.dat"
if __name__ == "__main__":
    main()