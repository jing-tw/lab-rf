import numpy as np
import argparse
import os
import matplotlib.pyplot as plt
import matplotlib



def show(filename, length):
    # 檔案路徑
    # filename = "./20250225/iq_f2.4_bw20m_g0_d3m_S45.0.dat"
    # 檢查檔案是否存在
    if not os.path.exists(filename):
        raise FileNotFoundError(f"檔案 {filename} 不存在")
        

    # 參數設定 (根據你的命令列)
    sample_rate = 28e6  # 28 MS/s
    center_freq = 2.4e9  # 2.4 GHz
    num_channels = 2    # 雙通道 (0 和 1)

    # 讀取數據
    # .dat 文件通常是交錯的複數數據 (I/Q)，每個樣本 8 bytes (float32 real + float32 imag)
    data = np.fromfile(filename, dtype=np.complex64)

    # singal channel
    num_samples = len(data)
    channel0 = data

    # 分離雙通道數據
    # 假設數據是交錯儲存的：通道0樣本1, 通道1樣本1, 通道0樣本2, 通道1樣本2...
    # num_samples = len(data) // num_channels
    # channel0 = data[0::2]  # 偶數索引為通道 0
    # channel1 = data[1::2]  # 奇數索引為通道 1

    # 創建時間軸
    time = np.arange(num_samples) / sample_rate

    # 繪製波形
    #plt.figure(figsize=(12, 8))

    


    # 通道 0
    # plt.subplot(2, 1, 1)
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))  # ax 是陣列 [ax[0], ax[1]]
    # 建立文字標籤，用來顯示座標
    text = ax[0].text(0.02, 0.95, '', transform=ax[0].transAxes)
    

    plt.plot(time[:length], np.real(channel0[:length]), label='I (Real)')
    # plt.plot(time[:length], np.imag(channel0[:length]), label='Q (Imag)')

    plt.title(f'Channel 0 Waveform (f_c = {center_freq/1e9} GHz, f_s = {sample_rate/1e6} MHz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

    # # 通道 1
    # plt.subplot(2, 1, 2)
    # plt.plot(time, np.real(channel1), label='I (Real)')
    # plt.plot(time, np.imag(channel1), label='Q (Imag)')
    # plt.title(f'Channel 1 Waveform (f_c = {center_freq/1e9} GHz, f_s = {sample_rate/1e6} MHz)')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Amplitude')
    # plt.legend()
    # plt.grid(True)

    # 調整佈局並顯示
    plt.tight_layout()
    plt.show()

    # 打印一些基本信息
    print(f"總樣本數: {len(data)}")
    print(f"每個通道的樣本數: {num_samples}")
    print(f"總時長: {num_samples/sample_rate*1e3:.2f} ms")

    # 定義滑鼠移動時的事件處理函數
    def on_move(event):
        # 檢查滑鼠是否在圖表區域內
        if event.inaxes != ax:
            return
        
        # 獲取滑鼠位置的 x, y 座標
        x_data = event.xdata
        y_data = event.ydata
        
        # 更新文字標籤
        text.set_text(f'x={x_data:.2f}, y={y_data:.2f}')
        plt.draw()
    # 連結事件處理函數到滑鼠移動事件
    fig.canvas.mpl_connect('motion_notify_event', on_move)

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
if __name__ == "__main__":
    main()